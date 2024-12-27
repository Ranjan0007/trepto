from django.shortcuts import render
from .models import SGXNifty
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz
from rest_framework import generics
from .models import SGXNifty
from .serializers import SGXNiftySerializer
from django.http import JsonResponse
from .sftp_util import connect_sftp, upload_file, close_sftp


def fetch_sgx_nifty_price():
    url = "https://sgxnifty.org/"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        last_trade = soup.find(text="Last Trade").find_next('td').text.strip()
        change = soup.find(text="Change").find_next('td').text.strip()
        change_percent = soup.find(text="Change in %").find_next('td').text.strip()
        
        india_tz = pytz.timezone('Asia/Kolkata')
        current_time = datetime.now(india_tz)
        
        return {
            "last_trade": last_trade,
            "change": change,
            "change_percent": change_percent,
            "time": current_time
        }
    return None

def index(request):
    sgx_nifty_data = fetch_sgx_nifty_price()
    if sgx_nifty_data:
        # Save to database
        SGXNifty.objects.create(
            last_trade=sgx_nifty_data['last_trade'],
            change=sgx_nifty_data['change'],
            change_percent=sgx_nifty_data['change_percent']
        )
    
    data = SGXNifty.objects.all().order_by('-timestamp')[:10]  # Get the last 10 records
    return render(request, 'index.html', {'data': data})


class SGXNiftyList(generics.ListAPIView):
    queryset = SGXNifty.objects.all().order_by('-timestamp')  # Get all records ordered by timestamp
    serializer_class = SGXNiftySerializer



def upload_to_sftp(request):
    # SFTP server details
    host = "132.148.176.221"
    port = 22
    username = "wr6u7au2k33t"
    password = "Hemalgupta@123"
    remote_path = "/home/wr6u7au2k33t/public_html/your_file.txt"  # Change to your desired remote path
    local_path = "path/to/your/local_file.txt"  # Change to your local file path

    # Connect to SFTP
    sftp = connect_sftp(host, port, username, password)
    if sftp:
        # Upload the file
        upload_file(sftp, local_path, remote_path)
        # Close the SFTP connection
        close_sftp(sftp)
        return JsonResponse({"status": "success", "message": "File uploaded successfully."})
    else:
        return JsonResponse({"status": "error", "message": "Failed to connect to SFTP server."})

# sgxnifty/sftp_util.py

import paramiko

def connect_sftp(host, port, username, password):
    try:
        # Create a Transport object
        transport = paramiko.Transport((host, port))
        # Connect to the server
        transport.connect(username=username, password=password)
        
        # Create an SFTP session
        sftp = paramiko.SFTPClient.from_transport(transport)
        return sftp
    except Exception as e:
        print(f"Failed to connect to SFTP server: {e}")
        return None
    

# sgxnifty/sftp_util.py (continued)

def upload_file(sftp, local_file_path, remote_file_path):
    try:
        sftp.put(local_file_path, remote_file_path)
        print(f"Successfully uploaded {local_file_path} to {remote_file_path}")
    except Exception as e:
        print(f"Failed to upload file: {e}")

def close_sftp(sftp):
    if sftp:
        sftp.close()
        print("SFTP connection closed.")
from django.urls import path
from .views import index, SGXNiftyList,upload_to_sftp

urlpatterns = [
    path('', index, name='index'),
     path('api/sgxnifty/', SGXNiftyList.as_view(), name='sgxnifty-list'),
     path('upload/', upload_to_sftp, name='upload-to-sftp'),  # New upload URL
    
]
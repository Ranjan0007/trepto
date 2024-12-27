# sgxnifty/serializers.py

from rest_framework import serializers
from .models import SGXNifty

class SGXNiftySerializer(serializers.ModelSerializer):
    class Meta:
        model = SGXNifty
        fields = ['id', 'change_percent', 'timestamp']
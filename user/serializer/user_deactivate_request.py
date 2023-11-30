from rest_framework import serializers

class UserDeactivate(serializers.Serializer):
    """"User deactivate input class"""
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    otp = serializers.CharField(max_length=100)
    

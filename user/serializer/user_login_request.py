from rest_framework import serializers

class LoginRequest(serializers.Serializer):
    password = serializers.CharField(max_length = 100)
    email = serializers.CharField(max_length = 100)
    username = serializers.CharField(max_length = 100)
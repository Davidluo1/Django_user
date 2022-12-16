from rest_framework import serializers
from django.core.validators import MaxValueValidator, MinValueValidator

class OtpVerifyRequest(serializers.Serializer):
    otp = serializers.IntegerField(validators=[
            MaxValueValidator(999999),
            MinValueValidator(100000)
        ])  #Find a way u restrict number entered by user
    email = serializers.CharField(max_length = 100)
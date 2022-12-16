from rest_framework import serializers
from django.core.validators import MaxValueValidator, MinValueValidator

class SignUpRequest(serializers.Serializer):
    password = serializers.CharField(max_length = 100)
    email = serializers.CharField(max_length = 100)
    first_name = serializers.CharField(max_length = 100)
    # restricted phone number length
    contact_number = serializers.IntegerField(validators=[
            MaxValueValidator(9999999999),
            MinValueValidator(1000000000)
        ])
    username = serializers.CharField(max_length = 100)
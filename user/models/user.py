from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """User input function specification"""
    
    # max length could take, unique does not take duplicate valuie, null = cannot be empty
    email = models.EmailField(max_length=300, unique=True, null=False)
    first_name = models.CharField(max_length=200, null=False)
    contact_number = models.CharField(max_length=200, null=False)
    otp_verify = models.BooleanField(default=False)
    username = models.CharField(max_length=200, unique=True, null=False)
    REQUIRED_FIELDS = ["first_name","contact_number"]
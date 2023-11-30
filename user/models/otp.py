from django.db import models

class OtpUser(models.Model):
    """Otp User"""
    otp_value = models.IntegerField()
    user = models.ForeignKey("user.User", models.DO_NOTHING)
     

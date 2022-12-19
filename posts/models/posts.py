from django.db import models

class UserPosts(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("user.User", models.DO_NOTHING)
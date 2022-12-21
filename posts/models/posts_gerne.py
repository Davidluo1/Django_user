from django.db import models

class Postsgerne(models.Model):
    posts = models.ForeignKey("posts.UserPosts", models.DO_NOTHING)
    gerne = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("user.User", models.DO_NOTHING)
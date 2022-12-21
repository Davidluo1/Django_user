from django.db import models

class PostsComment(models.Model):
    posts = models.ForeignKey("posts.UserPosts", models.DO_NOTHING)
    description = models.CharField(max_length = 1000)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("user.User", models.DO_NOTHING)
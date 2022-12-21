from django.db import models

class PostsReaction(models.Model):
    posts = models.ForeignKey("posts.UserPosts", models.DO_NOTHING)
    reaction = models.CharField(max_length = 1000)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("user.User", models.DO_NOTHING)
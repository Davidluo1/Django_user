from django.urls import path
from posts.views import CreatePostView, GetUpdatePostView

urlpatterns = [
    path('user<int:user_id>', CreatePostView.as_view()),
    path('user<int:user_id>/<int:post_id>', GetUpdatePostView.as_view()),
]


# 127.0.0.1:8000/api/v1/posts/ --> Create a post, GET request
#127.0.0.1:8000/api/v1/posts/<int:post_id> --> Get a post, Update a post and delete


# 1. Update adn delete posts -- API
# 2. define an APi to get certain user data

# 127.0.0.1:8000/api/v1/posts/user/<user_id> - All the posts done by user_id = 3
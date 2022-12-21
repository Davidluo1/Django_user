from django.urls import path
from posts.views import CreatePostView, GetUpdatePostView, CreateCommentView, CreateReactionView, CreateGerneView

urlpatterns = [
    path('', CreatePostView.as_view()),
    path('post<int:post_id>', GetUpdatePostView.as_view()),
    path('post<int:post_id>/comment', CreateCommentView.as_view()),
    path('post<int:post_id>/reaction', CreateReactionView.as_view()),
    path('post<int:post_id>/gerne', CreateGerneView.as_view()),
]

# 127.0.0.1:8000/api/v1/posts/ --> Create a post, GET request
#127.0.0.1:8000/api/v1/posts/<int:post_id> --> Get a post, Update a post and delete


# 1. Update adn delete posts -- API
# 2. define an APi to get certain user data

# 127.0.0.1:8000/api/v1/posts/user/<user_id> - All the posts done by user_id = 3
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from posts.models import UserPosts
from posts.serializer import AddPostsRequest
from rest_framework.permissions import IsAuthenticated


class CreatePostView(APIView):
    permission_classes = [(IsAuthenticated)]
    """Adding posts class"""

    def post(self, request, user_id):
        """Add posts to db"""
        req_data = request.data
        # user = request.user
        request_data = AddPostsRequest(data = req_data)
        _ = request_data.is_valid(raise_exception = True)
        req_data = request_data.validated_data
        qs = UserPosts.objects.create(title = req_data["title"], description = req_data["description"], user_id = user_id)
        return Response({"id" : qs.id, "title" : qs.title, "description" : qs.description}, status = 201)
        
    def get(self, request):
        """Get posts of user"""

        user = request.user
        qs = UserPosts.objects.filter(user = user)
        resp = []
        for data in qs:
            resp.append({"id" : data.id, "title" : data.title, "description" : data.description, "created_at" : data.created_at})
        return Response({"data" : resp}, status = 200)

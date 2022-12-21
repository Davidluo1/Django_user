from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from posts.models import UserPosts
from posts.serializer import AddPostsRequest
from rest_framework.permissions import IsAuthenticated
from user.models.user import User


class GetUpdatePostView(APIView):
    permission_classes = [(IsAuthenticated)]
    """Get, update and delete posts for user"""
        
    def get(self, request, user_id, post_id):
        """Get posts of user"""

        user = request.user
        qs = UserPosts.objects.filter(user_id = user_id, id = post_id)
        resp = []
        # print all the posts from a user
        for data in qs:
            resp.append({"id" : data.id, "title" : data.title, "description" : data.description, "created_at" : data.created_at})
        return Response({"data" : resp}, status = 200)
    
    def put(self, request, user_id, post_id):
        """Update posts of user"""
        user = request.data
        # get the specific post from the user
        qs = UserPosts.objects.filter(user_id = user_id, id = post_id, user = user)
        # update the title and description if the specific post exist
        if qs.exists():
            qs.update(title = user['title'], description = user['description'])
            return Response({"data" : "Updated"}, status = 200)
        return Response({"data" : "Update failed, post not exist"}, status = 400)
    
    def delete(self, request, user_id, post_id):
        """Delete posts of user"""
        user = request.user
        # specifc user post
        qs = UserPosts.objects.filter(user_id = user_id, id = post_id, user = user)
        if qs.exists():
            # delete the specific post
            qs.delete()
            return Response({"data" : "Deleted"}, status = 200)
        return Response({"data" : "delete failed, post not exist"}, status = 400)

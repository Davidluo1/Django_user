from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from posts.models import UserPosts
from posts.serializer import AddPostsRequest
from rest_framework.permissions import IsAuthenticated


class GetUpdatePostView(APIView):
    permission_classes = [(IsAuthenticated)]
    """Get, update and delete posts for user"""
        
    def get(self, request, post_id):
        """Get posts of user"""

        user = request.user
        qs = UserPosts.objects.filter(id = post_id)
        resp = []
        for data in qs:
            resp.append({"id" : data.id, "title" : data.title, "description" : data.description, "created_at" : data.created_at})
        return Response({"data" : resp}, status = 200)

    def put(self, request, post_id):

        user = request.user
        post_qs = UserPosts.objects.filter(id = post_id, user = user)
        if post_qs.exists():
            title = request.data.get("title", None)
            description = request.data.get("description", None)
            if title:
                UserPosts.objects.filter(id = post_id).update(title = title)
            if description:
                UserPosts.objects.filter(id = post_id).update(description = description)
            return Response({"msg" : "Information updated successfully"}, status = 200)
        else:
            return Response({"msg" : "Access denied"}, status = 401)
    
    def delete(self, request, post_id):

        user = request.user
        post_qs = UserPosts.objects.filter(id = post_id, user = user)
        if post_qs.exists():
            UserPosts.objects.filter(id = post_id, user = user).delete()
            return Response({"msg" : "Information deleted successfully"}, status = 200)
        else:
            return Response({"msg" : "Access denied"}, status = 401)
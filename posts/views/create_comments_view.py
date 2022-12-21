from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from posts.models import UserPosts, PostsComment
from posts.serializer import AddCommentRequest
from rest_framework.permissions import IsAuthenticated
from django.db import transaction


class CreateCommentView(APIView):
    permission_classes = [(IsAuthenticated)]
    """Adding comments to posts"""

    @transaction.atomic
    def post(self, request, post_id):
        """Add comments to db"""
        req_data = request.data
        user = request.user
        request_data = AddCommentRequest(data = req_data)
        _ = request_data.is_valid(raise_exception = True)
        req_data = request_data.validated_data
        post_qs = UserPosts.objects.filter(id = post_id)
        if post_qs.exists():
            comment_qs = PostsComment.objects.create(posts = post_qs[0], description =req_data["comment"], user = user )
            return Response({"id" : comment_qs.id, "comment" : comment_qs.description}, status = 200)
        else:
            return Response({"msg" : "Invalid posts id"}, status = 400)
        
    def get(self, request, post_id):
        """Get comments on a post"""

        qs = PostsComment.objects.filter(posts_id = post_id)
        resp = []
        for comment in qs:
            resp.append({"id" : comment.id, "description" : comment.description, "user" : comment.user.email})
        return Response({"data" : resp}, status=200)
    
    def put(self, request, post_id):
        user = request.user
        post_qs = PostsComment.objects.filter(id = post_id, user = user)
        if post_qs.exists():
            comment = request.data.get("description", None)
            if comment:
                PostsComment.objects.filter(id = post_id).update(description = comment)
            return Response({"msg" : "Information updated successfully"}, status = 200)
        else:
            return Response({"msg" : "Access denied"}, status = 401)
        
    def delete(self, request, post_id):

        user = request.user
        post_qs = PostsComment.objects.filter(id = post_id, user = user)
        if post_qs.exists():
            post_qs.filter(id = post_id, user = user).delete()
            return Response({"msg" : "Information deleted successfully"}, status = 200)
        else:
            return Response({"msg" : "Access denied"}, status = 401)
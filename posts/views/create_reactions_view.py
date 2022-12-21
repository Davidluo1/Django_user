from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from posts.models import UserPosts, PostsReaction
from posts.serializer import AddReactionRequest
from rest_framework.permissions import IsAuthenticated
from django.db import transaction


class CreateReactionView(APIView):
    permission_classes = [(IsAuthenticated)]
    """Adding reaction to posts"""

    # do not modify if error occurs
    @transaction.atomic
    # post a reaction function
    def post(self, request, post_id):
        """Add reaction to db"""
        req_data = request.data
        user = request.user
        request_data = AddReactionRequest(data = req_data)
        _ = request_data.is_valid(raise_exception = True)
        req_data = request_data.validated_data
        post_qs = UserPosts.objects.filter(id = post_id)
        if post_qs.exists():
            # do not post reaction if already exist
            list_check = PostsReaction.objects.filter(reaction = req_data["reaction"], user = user)
            if list_check:
                return Response({"msg" : "User reaction existed"}, status=400)
            # creates a user reaction
            reaction_qs = PostsReaction.objects.create(posts = post_qs[0], reaction =req_data["reaction"], user = user)
            return Response({"id" : reaction_qs.id, "reaction" : reaction_qs.reaction}, status = 200)
        else:
            return Response({"msg" : "Invalid posts id"}, status = 400)
        
    # get reaction list function
    def get(self, request, post_id):
        """Get reaction on a post"""
        # specific reaction of from the user
        qs = PostsReaction.objects.filter(posts_id = post_id)
        resp = []
        for reaction in qs:
            resp.append({"id" : reaction.id, "reaction" : reaction.reaction, "user" : reaction.user.email, "date" : reaction.created_at})
        return Response({"data" : resp}, status=200)
    
    # update reaction function
    def put(self, request, post_id):
        user = request.user
        # specific reaction of from the user
        qs = PostsReaction.objects.filter(id = post_id, user = user)
        if qs.exists():
            reaction = request.data.get("reaction", None)
            if reaction:
                # updates the reaction
                PostsReaction.objects.filter(id = post_id).update(reaction = reaction)
            return Response({"msg" : "Information updated successfully"}, status = 200)
        else:
            return Response({"msg" : "Access denied"}, status = 401)
    
    # delete a reaction function
    def delete(self, request, post_id):
        user = request.user
        # specific reaction of from the user
        qs = PostsReaction.objects.filter(id = post_id, user = user)
        if qs.exists():
            # deletes the reaction
            qs.filter(id = post_id, user = user).delete()
            return Response({"msg" : "Information deleted successfully"}, status = 200)
        else:
            return Response({"msg" : "Access denied"}, status = 401)
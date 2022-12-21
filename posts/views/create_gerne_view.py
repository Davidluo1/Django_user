from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from posts.models import UserPosts, Postsgerne
from posts.serializer import AddGerneRequest
from rest_framework.permissions import IsAuthenticated
from django.db import transaction


class CreateGerneView(APIView):
    permission_classes = [(IsAuthenticated)]
    """Adding gerne class"""
    
    def post(self, request, post_id):
        """Add gerne to db"""
        req_data = request.data
        user = request.user
        request_data = AddGerneRequest(data = req_data)
        _ = request_data.is_valid(raise_exception = True)
        req_data = request_data.validated_data
        qs = UserPosts.objects.filter(id = post_id)
        if qs.exists():
            # do not post if already exist
            if Postsgerne.objects.filter(gerne = req_data['gerne'], user = user):
                return Response({"msg" : "User post gerne existed"}, status=400)
            gerne_qs = Postsgerne.objects.create(posts = qs[0], gerne = req_data['gerne'], user = user)
            return Response({"id" : gerne_qs.id, "gerne" : gerne_qs.gerne}, status = 200)
        return Response({"msg" : "Failed"}, status=400)
    
    
    def get(self, request, post_id):
        qs = Postsgerne.objects.filter(id = post_id)
        if qs.exists():
            gerne_qs = qs[0]
            return Response({"id" : gerne_qs.id, "gerne" : gerne_qs.gerne, "created at" : gerne_qs.created_at})
        return Response({"msg" : "Failed, gerne not exist"}, status=400)
    
    
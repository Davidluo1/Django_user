from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User
from rest_framework.permissions import IsAuthenticated


class FetchUserView(APIView):
    """Fetch user information"""
    
    # Identify whether the user is authenticated or not
    permission_classes = [(IsAuthenticated)]
    
    def post(self,request):
        user = request.user
        return Response({"id" : user.id, "name" : user.first_name, "email" : user.email})
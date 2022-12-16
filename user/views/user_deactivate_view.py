from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializer.user_deactivate_request import UserDeactivate
from user.models import User, OtpUser


class UserDeactivateView(APIView):
    """User deactivate view"""
    
    def post(self, request):
        req_data = request.data
        request_data = UserDeactivate(data=req_data)
        # _ when not sure what input 
        _ = request_data.is_valid(raise_exception=True)
        req_data = request_data.validated_data
        otp = req_data['otp']
        email = req_data['email']
        password = req_data['password']
        user_qs = User.objects.filter(email = email)
        if user_qs.exists():
            user_instance = user_qs[0]
            password_verify = user_instance.check_password(password)
            if password_verify:
                otp_instance = OtpUser.objects.filter(user=user_instance, otp_value = otp)
                if otp_instance.exists():
                    user_qs.update(otp_verify=False)
                    return Response({"msg" : "Deactivate successful."})
                else:
                    return Response({"msg" : "OTP number not match"}, status=400)
            else:
                return Response({"msg" : "Incorrect password"}, status=400)
        return Response({"msg" : "Incorrect email."}, status=400)
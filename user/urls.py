from django.urls import path
from user.views import UserSignUpView, UserLoginView, User_OtpVerifyView, UserDeactivateView, FetchUserView

urlpatterns = [
    path('signup', UserSignUpView.as_view()),
    path('otp/verify', User_OtpVerifyView.as_view()),
    path('login', UserLoginView.as_view()),
    path('deactivate', UserDeactivateView.as_view()),
    path('userinfo', FetchUserView.as_view()),
]

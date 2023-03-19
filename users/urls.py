from django.urls import path
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LogoutView

from .views import UserLoginView, UserRegistrationView, UserProfileView, EmailVerificationView
from .models import EmailVerification


app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('email_verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verify'),
]


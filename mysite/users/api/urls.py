from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.generics import ListCreateAPIView

from users.models import Account
from .serializers import UserSerializer
from .views import urls_views, LogoutView, RegistrationView, UserProfileView, UserProfilePic, UserListView, \
    UserListFilterView

app_name = 'account'

urlpatterns = [
    path('register', RegistrationView.as_view(), name="register"),
    path('login', obtain_auth_token, name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('properties', UserProfileView.as_view(), name="properties"),
    path('picture', UserProfilePic.as_view(), name='user-picture'),
    path('users', UserListView.as_view(), name='user-list'),
    path('users/filter', UserListFilterView.as_view(), name='user-list'),
]

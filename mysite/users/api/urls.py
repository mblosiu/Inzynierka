from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import urls_views, LogoutView, RegistrationView, UserProfileView

app_name = 'users'

urlpatterns = [
    path('', obtain_auth_token, name="get users"),
    path('register', RegistrationView.as_view(), name="register"),
    path('login', obtain_auth_token, name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('properties', UserProfileView.as_view(), name="properties"),
]

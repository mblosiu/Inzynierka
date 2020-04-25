from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import urls_views, Logout, Registration

app_name = 'users'

urlpatterns = [
    path('', obtain_auth_token, name="get users"),
    path('register', Registration.as_view(), name="register"),
    path('login', obtain_auth_token, name="login"),
    path('logout', Logout.as_view(), name="logout"),
    path('urls', urls_views, name="urls"),
]

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import LogoutView, RegistrationView, UserProfileView, UserProfilePic, DeleteUserAccountView, \
    UserListView, PreferencesView, SettingsView, UserImage

app_name = 'users'

user_detail = UserListView.as_view({'get': 'retrieve'})
user_list = UserListView.as_view({'get': 'list'})

urlpatterns = [
    path('register', RegistrationView.as_view(), name="register"),
    path('login', obtain_auth_token, name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('delete', DeleteUserAccountView.as_view(), name="user-delete"),
    path('properties', UserProfileView.as_view(), name="user-properties"),
    path('preferences', PreferencesView.as_view(), name="user-preferences"),
    path('settings', SettingsView.as_view(), name="user-settings"),
    path('picture', UserProfilePic.as_view(), name='user-picture'),
    path('addpic', UserImage.as_view(), name='addpic'),
    path('users', user_list, name='user-list'),
    path('users/<int:pk>', user_detail, name='users-by-id'),
]

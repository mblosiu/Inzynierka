from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import LogoutView, RegistrationView, UserProfileView, UserProfilePic, DeleteUserAccountView, \
    UserListView, PreferencesView, SettingsView, UserImage, ValidUsernameAndEmail, ImageByUserId, LikesView

app_name = 'users'

user_detail = UserListView.as_view({'get': 'retrieve'})
user_list = UserListView.as_view({'get': 'list'})
images_list = ImageByUserId.as_view({'get': 'retrieve'})
create_like = LikesView.as_view({'post': 'create_like'})
delete_like = LikesView.as_view({'delete': 'delete_like'})
get_users_are_liked = LikesView.as_view({'get': 'get_users_are_liked'})
get_users_liked = LikesView.as_view({'get': 'get_users_liked'})
get_user_are_liked = LikesView.as_view({'get': 'get_user_are_liked'})
get_user_liked = LikesView.as_view({'get': 'get_user_liked'})

urlpatterns = [
    path('register', RegistrationView.as_view(), name="register"),
    path('login', obtain_auth_token, name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('delete', DeleteUserAccountView.as_view(), name="user-delete"),
    path('properties', UserProfileView.as_view(), name="user-properties"),
    path('preferences', PreferencesView.as_view(), name="user-preferences"),
    path('settings', SettingsView.as_view(), name="user-settings"),
    path('profile-image', UserProfilePic.as_view(), name='profile-image'),
    path('images', UserImage.as_view(), name='images'),
    path('users', user_list, name='user-list'),
    path('users/<int:pk>', user_detail, name='users-by-id'),
    path('users/<int:pk>/images', images_list, name='user-by-id-images'),
    path('validregister', ValidUsernameAndEmail.as_view(), name='valid-register'),

    path('create-like', create_like, name='create-like'),
    path('delete-like', delete_like, name='delete-like'),
    path('get-users-are-liked/<int:pk>', get_users_are_liked, name='are-liked1'),
    path('get-users-liked/<int:pk>', get_users_liked, name='get_users_liked1'),
    path('get-user-are-liked', get_user_are_liked, name='are-liked2'),
    path('get-user-liked', get_user_liked, name='get_users_liked2'),
]

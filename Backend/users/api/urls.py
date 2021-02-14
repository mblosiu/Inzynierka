from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import LogoutView, RegistrationView, UserProfileView, UserProfilePic, DeleteUserAccountView, \
    UserListView, PreferencesView, SettingsView, UserImage, ImageByUserId, LikesView, \
    AdminReportView, BlackListView, FriendListView, RandomPair, ChangePasswordView, RestorePasswordView, \
    VerifyAccountView, ReportView, RegistrationValidationView, CustomAuthToken
from rest_framework.authtoken.views import ObtainAuthToken
app_name = 'users'

user_detail = UserListView.as_view({'get': 'retrieve'})
user_list = UserListView.as_view({'get': 'list'})
create_like = LikesView.as_view({'post': 'create_like'})
delete_like = LikesView.as_view({'delete': 'delete_like'})
get_liked_users = LikesView.as_view({'get': 'get_liked_users'})
get_like_users = LikesView.as_view({'get': 'get_like_users'})
get_liked_user = LikesView.as_view({'get': 'get_liked_user'})
get_like_user = LikesView.as_view({'get': 'get_like_user'})

urlpatterns = [
    # zarządzanie kontem
    path('register', RegistrationView.as_view(), name="register"),
    path('login', CustomAuthToken.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('delete', DeleteUserAccountView.as_view(), name="delete"),
    path('properties', UserProfileView.as_view(), name="properties"),
    path('preferences', PreferencesView.as_view(), name="preferences"),
    path('settings', SettingsView.as_view(), name="settings"),
    path('profile-image', UserProfilePic.as_view(), name='profile-image'),
    path('images', UserImage.as_view(), name='images'),
    path('users', user_list, name='users'),
    path('users/<int:pk>', user_detail, name='users-by-id'),
    path('users/<int:pk>/images', ImageByUserId.as_view(), name='user-images-by-id'),
    path('change-password', ChangePasswordView.as_view(), name='change-password'),
    path('restore-password', RestorePasswordView.as_view(), name='restore-password'),
    path('account-verify', VerifyAccountView.as_view(), name='account-verify'),
    path('registration-validation', RegistrationValidationView.as_view(), name='registration-validation'),

    # interakcja między użytkownikami
    path('create-like', create_like, name='create-like'),
    path('delete-like', delete_like, name='delete-like'),
    path('get-users-are-liked/<int:pk>', get_liked_users, name='get-users-are-liked'),
    path('get-users-liked/<int:pk>', get_like_users, name='get-users-liked'),
    path('get-user-are-liked', get_liked_user, name='get-user-are-liked'),
    path('get-user-liked', get_like_user, name='get_users_liked'),
    path('blacklist', BlackListView.as_view(), name='blacklist'),
    path('friendlist', FriendListView.as_view(), name='friendlist'),
    path('random-pair', RandomPair.as_view(), name='random-pair'),
    path('report', ReportView.as_view(), name='report'),
    path('admin/report', AdminReportView.as_view(), name='report-admin'),
]

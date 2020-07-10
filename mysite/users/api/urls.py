from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import LogoutView, RegistrationView, UserProfileView, UserProfilePic, RemoveUserAccountView, \
    UserPreferencesView, UserListView, SearchUserListView, FilterUserListView

app_name = 'users'

urlpatterns = [
    path('register', RegistrationView.as_view(), name="register"),
    path('login', obtain_auth_token, name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('delete', RemoveUserAccountView.as_view(), name="remove-account"),
    path('properties', UserProfileView.as_view(), name="properties"),
    path('preferences', UserPreferencesView.as_view(), name="preferences"),
    path('picture', UserProfilePic.as_view(), name='user-picture'),
    path('users', UserListView.as_view(), name='user-list'),
    path('users-filters', FilterUserListView.as_view(), name='user-list-filters'),
    path('users-search', SearchUserListView.as_view(), name='user-list-filters'),
]

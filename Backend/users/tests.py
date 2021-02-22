import tempfile

from PIL import Image
from rest_framework import status
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate
from rest_framework.authtoken.models import Token

from users.api.urls import user_detail, user_list
# from .api.views import CustomAuthToken
from users.api.views import RegistrationView, UserProfileView, PreferencesView, SettingsView, DeleteUserAccountView, \
    UserProfilePic, UserListView, CustomAuthToken, LogoutView, LikesView, BlackListView, FriendListView
from users.models import User, Preferences, Settings
from users.api.urls import user_detail, user_list, create_like, delete_like, get_liked_users, get_like_users, \
    get_liked_user, get_like_user


# Create your tests here.

class UsersTestCase(APITestCase):
    def setUp(self):
        User1 = User.objects.create_user(username="testcase1", email="testcase1@gmail.com", location="Poznań",
                                         birthday="1996-06-20",
                                         sex="female", password="password")
        User2 = User.objects.create_user(username="testcase2", email="testcase2@gmail.com", location="Poznań",
                                         birthday="1996-06-20",
                                         sex="female", password="password")
        User3 = User.objects.create_user(username="testcase3", email="testcase3@gmail.com", location="Poznań",
                                         birthday="1996-06-20",
                                         sex="female", password="password")
        User4 = User.objects.create_user(username="testcase4", email="testcase4@gmail.com", location="Poznań",
                                         birthday="1996-06-20",
                                         sex="female", password="password")
        p = Preferences()
        p.save()
        s = Settings(dark_theme=False, )
        s.save()
        User1.preferences = p
        User1.settings = s
        User1.save()

    def test_RegistrationView(self):
        factory = APIRequestFactory()

        view = RegistrationView.as_view()

        data = {"username": "testcase", "email": "testcase@gmail.com", "location": "Polska", "birthday": "1996-06-20",
                "sex": "male", "password": "password", "password2": "password"}

        request = factory.post('/api/user/register', data)

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_CustomAuthToken(self):
        factory = APIRequestFactory()

        view = obtain_auth_token

        data = {"username": "testcase1", "password": "password"}

        request = factory.post('/api/user/login', data)

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_LogoutView(self):
        # TODO: logout unit test
        self.assertEqual(1, 1)

    def test_DeleteUserAccountView(self):
        factory = APIRequestFactory()

        user = User.objects.get(username='testcase1')

        view = DeleteUserAccountView.as_view()

        request = factory.delete('/api/user/delete', {'password': 'password'})

        force_authenticate(request, user=user)

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_UserProfileView_GET(self):
        factory = APIRequestFactory()

        user = User.objects.get(username='testcase1')

        view = UserProfileView.as_view()

        request = factory.get('/api/user/properties')

        force_authenticate(request, user=user)

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_UserProfileView_PATCH(self):
        factory = APIRequestFactory()

        user = User.objects.get(username='testcase1')

        view = UserProfileView.as_view()

        data = {
            'sex': 'Mężczyzna',
            'hair_color': 'Czarne'
        }

        request = factory.patch('/api/user/properties', data)

        force_authenticate(request, user=user)

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_PreferencesView_GET(self):
        factory = APIRequestFactory()

        user = User.objects.get(username='testcase1')

        view = PreferencesView.as_view()

        request = factory.get('/api/user/preferences')

        force_authenticate(request, user=user)

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_PreferencesView_PATCH(self):
        factory = APIRequestFactory()

        user = User.objects.get(username='testcase1')

        view = PreferencesView.as_view()

        data = {
            'hair_color_blonde_preference': '1',
            'growth_preference': '1'
        }

        request = factory.patch('/api/user/preferences', data)

        force_authenticate(request, user=user)

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_SettingsView_GET(self):
        factory = APIRequestFactory()

        user = User.objects.get(username='testcase1')

        view = SettingsView.as_view()

        request = factory.get('/api/user/settings')

        force_authenticate(request, user=user)

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_SettingsView_PATCH(self):
        factory = APIRequestFactory()

        user = User.objects.get(username='testcase1')

        view = SettingsView.as_view()

        data = {
            'dark_theme': True,
        }

        request = factory.patch('/api/user/settings', data)

        force_authenticate(request, user=user)

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_LikesView_user_detail(self):
        factory = APIRequestFactory()

        user = User.objects.get(username='testcase1')

        view = SettingsView.as_view()

        request = factory.get('/api/user/users/2')

        force_authenticate(request, user=user)

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_UserListView_user_list(self):
        factory = APIRequestFactory()

        user = User.objects.get(username='testcase1')

        view = user_list

        request = factory.get('/api/user/users')

        force_authenticate(request, user=user)

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_like(self):
        factory = APIRequestFactory()

        user1 = User.objects.get(username='testcase1')
        user2 = User.objects.get(username='testcase2')

        view = create_like

        data = {
            'pk': user2.pk,
            'value': 'like'
        }

        request = factory.post('/api/user/create-like', data)

        force_authenticate(request, user=user1)

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_liked_users(self):
        factory = APIRequestFactory()

        user = User.objects.get(username='testcase1')

        view = get_liked_users

        request = factory.get('/api/user/get-users-are-liked/' + str(user.pk))

        force_authenticate(request, user=user)

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_like_users(self):
        factory = APIRequestFactory()

        user = User.objects.get(username='testcase1')

        view = get_like_users

        request = factory.get('/api/user/get-users-liked/' + str(user.pk))

        force_authenticate(request, user=user)

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_liked_user(self):
        factory = APIRequestFactory()

        user = User.objects.get(username='testcase1')

        view = get_liked_user

        request = factory.get('/api/user/get-user-are-liked/')

        force_authenticate(request, user=user)

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_like_user(self):
        factory = APIRequestFactory()

        user = User.objects.get(username='testcase1')

        view = get_like_user

        request = factory.get('/api/user/get-user-liked/')

        force_authenticate(request, user=user)

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

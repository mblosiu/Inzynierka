import tempfile

from PIL import Image
from rest_framework import status
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate

from .api.urls import user_detail, user_list
from .api.views import RegistrationView, UserProfileView, PreferencesView, DeleteUserAccountView, UserProfilePic
from .models import User


# Create your tests here.

class AuthenticationTestCase(APITestCase):
    def setUp(self):
        User.objects.create_user(username="testcase1", email="testcase1@gmail.com", location="Poznań",
                                 birthday="1996-06-20",
                                 sex="female", password="password")

    def test_registration(self):
        factory = APIRequestFactory()

        view = RegistrationView.as_view()

        data = {"username": "testcase", "email": "testcase@gmail.com", "location": "Polska", "birthday": "1996-06-20",
                "sex": "male", "password": "password", "password2": "password"}

        request = factory.post('/api/user/register', data)

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        factory = APIRequestFactory()

        view = obtain_auth_token

        data = {"username": "testcase1", "password": "password"}

        request = factory.post('/api/user/login', data)

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        # TODO: logout unit test
        self.assertEqual(1, 1)

    def test_delete(self):
        factory = APIRequestFactory()

        user = User.objects.get(username='testcase1')

        view = DeleteUserAccountView.as_view()

        request = factory.delete('/api/user/delete')

        force_authenticate(request, user=user)

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserViewTestCase(APITestCase):
    def setUp(self):
        User.objects.create_user(username="testcase1", email="testcase1@gmail.com", location="Poznań",
                                 birthday="1996-06-20",
                                 sex="female", password="password")

    def test_profile_patch(self):
        factory = APIRequestFactory()

        user = User.objects.get(username='testcase1')

        view = UserProfileView.as_view()

        data = {'name': 'Mateusz', 'surname': 'Błoszyk', "description": ""}

        request = factory.patch('/api/user/properties', data)

        force_authenticate(request, user=user)

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_get(self):
        factory = APIRequestFactory()

        user = User.objects.get(username='testcase1')

        view = UserProfileView.as_view()

        request = factory.get('/api/user/properties')

        force_authenticate(request, user=user)

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_preferences_patch(self):
        factory = APIRequestFactory()

        user = User.objects.get(username='testcase1')

        view = PreferencesView.as_view()

        data = {"orientation": "Male"}

        request = factory.patch('/api/user/preferences', data)

        force_authenticate(request, user=user)

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_preferences_get(self):
        factory = APIRequestFactory()

        user = User.objects.get(username='testcase1')

        view = PreferencesView.as_view()

        request = factory.get('/api/user/preferences')

        force_authenticate(request, user=user)

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_picture_patch(self):
        factory = APIRequestFactory()

        user = User.objects.get(username='testcase1')

        view = UserProfilePic.as_view()

        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        tmp_file.seek(0)

        request = factory.patch('/api/user/picture', {'profile_picture': tmp_file}, format='multipart')

        force_authenticate(request, user=user)

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_picture_get(self):
        factory = APIRequestFactory()

        user = User.objects.get(username='testcase1')

        view = UserProfilePic.as_view()

        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        tmp_file.seek(0)
        request = factory.patch('/api/user/picture', {'profile_picture': tmp_file}, format='multipart')
        force_authenticate(request, user=user)

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UsersViewTestCase(APITestCase):
    def setUp(self):
        User.objects.create_user(username="testcase1", email="testcase1@gmail.com", location="Poznań",
                                 birthday="1996-06-20",
                                 sex="female", password="password")
        User.objects.create_user(username="testcase2", email="testcase2@gmail.com", location="Warszawa",
                                 birthday="1991-06-20",
                                 sex="male", password="password")
        User.objects.create_user(username="testcase3", email="testcase3@gmail.com", location="Poznań",
                                 birthday="1970-06-20",
                                 sex="male", password="password")
        User.objects.create_user(username="testcase4", email="testcase4@gmail.com", location="Wrocław",
                                 birthday="1980-06-20",
                                 sex="male", password="password")
        User.objects.create_user(username="testcase5", email="testcase5@gmail.com", location="Warszawa",
                                 birthday="1999-06-20",
                                 sex="female", password="password")

    def test_detail(self):
        factory = APIRequestFactory()

        user = User.objects.get(username='testcase1')

        view = user_detail

        data = {}

        request = factory.get('/api/user/users/3', data)

        force_authenticate(request, user=user)

        response = view(request, pk=3)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list(self):
        factory = APIRequestFactory()

        user = User.objects.get(username='testcase1')

        view = user_list

        data = {}

        request = factory.get('/api/user/users', data)

        force_authenticate(request, user=user)

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_search(self):
        factory = APIRequestFactory()

        user = User.objects.get(username='testcase1')

        view = user_list

        data = {}

        request = factory.get('/api/user/users?search=Mateusz', data)

        force_authenticate(request, user=user)

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_filter(self):
        factory = APIRequestFactory()

        user = User.objects.get(username='testcase1')

        view = user_list

        data = {}

        request = factory.get('/api/user/users?location=Wrocław&birthday=1980-06-20', data)

        force_authenticate(request, user=user)

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

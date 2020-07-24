from rest_framework import status
from rest_framework.test import APITestCase

from .models import User


# Create your tests here.

class UserAccountTestCase(APITestCase):
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

    def test_registration(self):
        data = {"username": "testcase", "email": "testcase@gmail.com", "location": "Polska", "birthday": "1996-06-20",
                "sex": "male", "password": "password", "password2": "password"}
        response = self.client.post("/api/user/register", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        response = self.client.post("/api/user/login", {"username": "testcase1", "password": "password"})
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

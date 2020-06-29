from django.test import TestCase
import json
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from mysite.users.models import User


# Create your tests here.

class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data = {"username": "testcase", "email": "testcase@gmail.com", "location": "Polska", "birthday": "1996-06-20",
                "sex": "male", "password": "password", "password2": "password"}
        response = self.client.post("/api/account/register/", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

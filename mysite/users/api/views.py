from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from .serializers import RegistrationSerializer, UserSerializer
from ..models import Account


def urls_views(request):
    return HttpResponse(
        "<html><body>URLS:<br>/admin<br>/api/users<br>/api/users/register<br>/api/users/login<br><br><br><br></body></html>")


@permission_classes([])
class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered new user.'
            data['email'] = account.email
            data['username'] = account.username
            data['name'] = account.name
            data['surname'] = account.surname
            data['birthday'] = account.birthday
        else:
            data = serializer.errors
        return Response(data)


@permission_classes([IsAuthenticated])
class LogoutView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class UserProfileView(APIView):
    def get(self, request):
        try:
            account = request.user
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(account)
        return Response(serializer.data)

    def post(self, request):
        try:
            account = request.user
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        response = {}
        if request.data["email"] != "" and request.data["email"] != account.email:
        #TODO: add unique validation
            account.email = request.data["email"]
            response["email"] = "error"
        else:
            response["email"] = "no changes"
        if request.data["name"] != "" and request.data["name"] != account.name:
            account.name = request.data["name"]
            response["name"] = "updated"
        else:
            response["name"] = "no changes"
        if request.data["surname"] != "" and request.data["surname"] != account.surname:
            account.surname = request.data["surname"]
            response["surname"] = "updated"
        else:
            response["surname"] = "no changes"
        if request.data["sex"] != "" and request.data["sex"] != account.sex:
            account.sex = request.data["sex"]
            response["sex"] = "updated"
        else:
            response["sex"] = "no changes"
        account.save()

        return Response(response)

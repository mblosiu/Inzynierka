from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from .serializers import RegistrationSerializer, UserProfileSerializer
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
        serializer = UserProfileSerializer(account)
        return Response(serializer.data)

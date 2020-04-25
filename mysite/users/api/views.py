from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from .serializers import RegistrationSerializer
from ..models import Account


def urls_views(request):
    return HttpResponse(
        "<html><body>URLS:<br>/admin<br>/api/users<br>/api/users/register<br>/api/users/login<br><br><br><br></body></html>")


@permission_classes([])
@authentication_classes([])
class Registration(APIView):
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


class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

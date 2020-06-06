from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import generics

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
            data['birthday'] = account.birthday
            data['location'] = account.location
            stat = status.HTTP_201_CREATED
        else:
            data = serializer.errors
            stat = status.HTTP_400_BAD_REQUEST
        return Response(data, status=stat)


@permission_classes([IsAuthenticated])
class LogoutView(APIView):
    def get(self, request):
        if request.user.auth_token.delete():
            stat = status.HTTP_200_OK
            return Response({"detail": "success"}, status=stat)
        else:
            stat = status.HTTP_400_BAD_REQUEST
            return Response({"detail": "invalid token"}, status=stat)


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

        try:
            if request.data["email"] != "" and request.data["email"] != account.email:
                userlist = Account.objects.filter(email=request.data["email"])
                if not userlist:
                    account.email = request.data["email"]
                    response["email"] = "updated"
                else:
                    response["email"] = "This email is occupied"
            else:
                response["email"] = "no changes"
        except KeyError:
            pass
        try:
            if request.data["name"] != account.name:
                account.name = request.data["name"]
                response["name"] = "updated"
            else:
                response["name"] = "no changes"
        except KeyError:
            pass
        try:
            if request.data["surname"] != "" and request.data["surname"] != account.surname:
                account.surname = request.data["surname"]
                response["surname"] = "updated"
            else:
                response["surname"] = "no changes"
        except KeyError:
            pass
        try:
            if request.data["sex"] != "" and request.data["sex"] != account.sex:
                account.sex = request.data["sex"]
                response["sex"] = "updated"
            else:
                response["sex"] = "no changes"
        except KeyError:
            pass

        if response:
            account.save()
            stat = status.HTTP_200_OK
        else:
            response["detail"] = "request must contain user data"
            stat = status.HTTP_400_BAD_REQUEST
        return Response(response, status=stat)


# all users list
@permission_classes([IsAuthenticated])
class UsersList(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get(self, request):
        queryset = Account.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

# TODO: filters

@permission_classes([IsAuthenticated])
class UsersListFilter(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get(self, request):
        location = request.data['location']
        queryset = Account.objects.filter(location=location)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

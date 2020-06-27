from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import RegistrationSerializer, UserSerializer
from ..models import Account
from django.db.models import Q


def urls_views(request):
    return HttpResponse(
        "<html><body>URLS:<br>/admin<br>/api/users<br>/api/account/register<br>/api/account/login<br><br><br><br></body></html>")


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
                account.name = request.data["name"][0].upper() + request.data["name"][1:]
                response["name"] = "updated"
            else:
                response["name"] = "no changes"
        except KeyError:
            pass
        try:
            if request.data["surname"] != "" and request.data["surname"] != account.surname:
                account.surname = request.data["surname"][0].upper() + request.data["surname"][1:]
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
        try:
            if request.data["description"] != "" and request.data["description"] != account.description:
                account.description = request.data["description"]
                response["description"] = "updated"
            else:
                response["description"] = "no changes"
        except KeyError:
            pass

        if response:
            account.save()
            stat = status.HTTP_200_OK
        else:
            response["detail"] = "request must contain user data"
            stat = status.HTTP_400_BAD_REQUEST
        return Response(response, status=stat)


@permission_classes([IsAuthenticated])
class UserProfilePic(APIView):
    def post(self, request):
        try:
            account = request.user
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        response = {}

        file = request.data.get('profile_picture', None)

        # validate content type
        main, sub = file.content_type.split('/')

        if not file:
            response["detail"] = "request must contain user data"
            stat = status.HTTP_400_BAD_REQUEST

        elif not (main == 'image' and sub in ['jpeg', 'pjpeg', 'jpg', 'png']):
            response["detail"] = "wrong data type"
            stat = status.HTTP_400_BAD_REQUEST

        else:
            account.profile_picture = file
            response["detail"] = "photo added successfuly"
            account.save()
            stat = status.HTTP_200_OK

        return Response(response, status=stat)


# USER LIST - SEARCHER
@permission_classes([IsAuthenticated])
class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['name', 'surname', 'birthday', 'sex', 'location',
                     'hair_color', 'body_type', 'race_origin', 'is_smoking',
                     'is_drinking_alcohol']
    queryset = Account.objects.all()


# USER LIST - FILTERS
@permission_classes([IsAuthenticated])
class UserListFilterView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get(self, request):
        queryset = Account.objects.all()

        name = request.data.get('name', None)
        surname = request.data.get('surname', None)
        location = request.data.get('location', None)
        sex = request.data.get('sex', None)
        hair_color = request.data.get('hair_color', None)
        growth = request.data.get('growth', None)
        weight = request.data.get('weight', None)
        body_type = request.data.get('body_type', None)
        race_origin = request.data.get('race_origin', None)
        is_smoking = request.data.get('is_smoking', None)
        is_drinking_alcohol = request.data.get('is_drinking_alcohol', None)

        if not (name is None or name == ''):
            queryset = queryset.filter(name=name)
        if not (surname is None or surname == ''):
            queryset = queryset.filter(surname=surname)
        if not (location is None or location == ''):
            queryset = queryset.filter(location=location)
        if not (sex is None or sex == ''):
            queryset = queryset.filter(sex=sex)
        if not (hair_color is None or hair_color == ''):
            queryset = queryset.filter(hair_color=hair_color)
        if not (growth is None or growth == ''):
            queryset = queryset.filter(growth=growth)
        if not (weight is None or weight == ''):
            queryset = queryset.filter(weight=weight)
        if not (body_type is None or body_type == ''):
            queryset = queryset.filter(body_type=body_type)
        if not (race_origin is None or race_origin == ''):
            queryset = queryset.filter(race_origin=race_origin)
        if not (is_smoking is None or is_smoking == ''):
            queryset = queryset.filter(is_smoking=is_smoking)
        if not (is_drinking_alcohol is None or is_drinking_alcohol == ''):
            queryset = queryset.filter(is_drinking_alcohol=is_drinking_alcohol)

        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

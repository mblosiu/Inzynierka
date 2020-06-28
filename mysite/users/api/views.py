from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import RegistrationSerializer, UserSerializer
from ..models import Account


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
class RemoveUserAccountView(APIView):
    def get(self, request):
        if request.user.delete():
            # TODO : check password
            stat = status.HTTP_200_OK
            return Response({"detail": "success"}, status=stat)
        else:
            stat = status.HTTP_400_BAD_REQUEST
            return Response({"detail": "invalid token"}, status=stat)


@permission_classes([IsAuthenticated])
class UserProfileView(APIView):
    serializer_class = UserSerializer

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

        email = request.data.get('email', None)
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
        description = request.data.get('description', None)

        if email in [None, '', account.email]:
            response["email"] = "no changes"
        else:
            userlist = Account.objects.filter(email=email)
            if userlist:
                response["email"] = "This email is occupied"
            else:
                account.email = email
                response["email"] = "updated"

        if name in [None, '', account.name]:
            response["name"] = "no changes"
        else:
            account.name = name.capitalize()
            response["name"] = "updated"

        if surname in [None, '', account.surname]:
            response["surname"] = "no changes"
        else:
            account.surname = surname.capitalize()
            response["surname"] = "updated"

        if location in [None, '', account.location]:
            response["location"] = "no changes"
        else:
            account.location = location.capitalize()
            response["location"] = "updated"

        if sex in [None, '', account.sex]:
            response["sex"] = "no changes"
        else:
            account.sex = sex.capitalize()
            response["sex"] = "updated"

        if hair_color in [None, '', account.hair_color]:
            response["hair_color"] = "no changes"
        else:
            account.hair_color = hair_color.capitalize()
            response["hair_color"] = "updated"

        if growth in [None, '', account.growth]:
            response["growth"] = "no changes"
        else:
            account.growth = growth
            response["growth"] = "updated"

        if weight in [None, '', account.weight]:
            response["weight"] = "no changes"
        else:
            account.weight = weight
            response["weight"] = "updated"

        if body_type in [None, '', account.body_type]:
            response["body_type"] = "no changes"
        else:
            account.body_type = body_type.capitalize()
            response["body_type"] = "updated"

        if race_origin in [None, '', account.race_origin]:
            response["race_origin"] = "no changes"
        else:
            account.race_origin = race_origin.capitalize()
            response["race_origin"] = "updated"

        if is_smoking in [None, '', account.is_smoking]:
            response["is_smoking"] = "no changes"
        else:
            account.is_smoking = is_smoking.capitalize()
            response["is_smoking"] = "updated"

        if is_drinking_alcohol in [None, '', account.is_drinking_alcohol]:
            response["is_drinking_alcohol"] = "no changes"
        else:
            account.is_drinking_alcohol = is_drinking_alcohol.capitalize()
            response["is_drinking_alcohol"] = "updated"

        if description in [None, '', account.description]:
            response["description"] = "no changes"
        else:
            account.description = description
            response["description"] = "updated"

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

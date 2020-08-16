from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegistrationSerializer, UserSerializer, UserPreferencesSerializer, UserProfilePicSerializer, \
    UserSettingsSerializer
from ..models import User, Preferences, Settings


@permission_classes([])
class RegistrationView(APIView):
    @staticmethod
    def post(request):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()

            data['detail'] = 'successfully registered new user.'

            stat = status.HTTP_201_CREATED
        else:
            data = serializer.errors
            stat = status.HTTP_400_BAD_REQUEST
        return Response(data, status=stat)


@permission_classes([IsAuthenticated])
class LogoutView(APIView):
    @staticmethod
    def post(request):
        if request.user.auth_token.delete():
            return Response({"detail": "success"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "invalid token"}, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
class DeleteUserAccountView(APIView):
    @staticmethod
    def delete(request):
        if request.user.delete():
            # TODO : check password
            return Response({"detail": "Account removed successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "invalid token"}, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
class UserProfileView(APIView):

    @staticmethod
    def get(request):
        try:
            account = request.user
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def patch(request):
        try:
            account = request.user
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        response = {}

        email = request.data.get('email', None)
        name = request.data.get('name', '').capitalize()
        surname = request.data.get('surname', '').capitalize()
        location = request.data.get('location', '').capitalize()
        sex = request.data.get('sex', '').capitalize()
        hair_color = request.data.get('hair_color', '').capitalize()


        try:
            body_type = request.data.get('body_type', '').capitalize()
        except ValueError:
            print("xd")
        growth = request.data.get('growth', '')
        weight = request.data.get('weight', '')
        description = request.data.get('description', '')
        is_smoking = request.data.get('is_smoking', False)
        is_drinking_alcohol = request.data.get('is_drinking_alcohol', False)



        if email in [None, '', account.email]:
            response["email"] = "no changes"
        else:
            userlist = User.objects.filter(email=email)
            if userlist:
                response["email"] = "This email is occupied"
            else:
                account.email = email
                response["email"] = "updated"

        if name in [account.name]:
            response["name"] = "no changes"
        else:
            account.name = name
            response["name"] = "updated"

        if surname in [None, '', account.surname]:
            response["surname"] = "no changes"
        else:
            account.surname = surname
            response["surname"] = "updated"

        if location in [None, '', account.location]:
            response["location"] = "no changes"
        else:
            account.location = location
            response["location"] = "updated"

        if sex in [None, '', account.sex]:
            response["sex"] = "no changes"
        else:
            account.sex = sex
            response["sex"] = "updated"

        if hair_color in [None, '', account.hair_color]:
            response["hair_color"] = "no changes"
        else:
            account.hair_color = hair_color
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
            account.body_type = body_type
            response["body_type"] = "updated"

        if is_smoking in [None, '', account.is_smoking]:
            response["is_smoking"] = "no changes"
        else:
            account.is_smoking = is_smoking
            response["is_smoking"] = "updated"

        if is_drinking_alcohol in [None, '', account.is_drinking_alcohol]:
            response["is_drinking_alcohol"] = "no changes"
        else:
            account.is_drinking_alcohol = is_drinking_alcohol
            response["is_drinking_alcohol"] = "updated"

        if description in [None, '', account.description]:
            response["description"] = "no changes"
        else:
            account.description = description
            response["description"] = "updated"

        if response:
            account.save()
            return Response(response, status=status.HTTP_200_OK)
        else:
            response["detail"] = "request must contain user data"
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
class PreferencesView(APIView):
    @staticmethod
    def patch(request):
        try:
            account = request.user
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            preferences = request.user.preferences
        except Preferences.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        response = {}

        orientation = request.data.get('orientation', '').capitalize()
        hair_color_blonde_preference = request.data.get('hair_color_blonde_preference', '').capitalize()
        hair_color_brunette_preference = request.data.get('hair_color_brunette_preference', '').capitalize()
        hair_color_red_preference = request.data.get('hair_color_red_preference', '').capitalize()
        growth_preference = request.data.get('growth_preference', '').capitalize()
        weight_preference = request.data.get('weight_preference', '').capitalize()
        body_type_preference = request.data.get('body_type_preference', '').capitalize()
        is_smoking_preference = request.data.get('is_smoking_preference', '').capitalize()
        is_drinking_alcohol_preference = request.data.get('is_drinking_alcohol_preference', '').capitalize()

        if orientation == preferences.orientation:
            response["orientation"] = "no changes"
        else:
            preferences.orientation = orientation
            response["orientation"] = "updated"

        if hair_color_blonde_preference == preferences.hair_color_blonde_preference:
            response["hair_color_blonde_preference"] = "no changes"
        else:
            preferences.hair_color_blonde_preference = hair_color_blonde_preference
            response["hair_color_blonde_preference"] = "updated"

        if hair_color_brunette_preference == preferences.hair_color_brunette_preference:
            response["hair_color_brunette_preference"] = "no changes"
        else:
            preferences.hair_color_brunette_preference = hair_color_brunette_preference
            response["hair_color_brunette_preference"] = "updated"

        if hair_color_red_preference == preferences.hair_color_red_preference:
            response["hair_color_red_preference"] = "no changes"
        else:
            preferences.hair_color_red_preference = hair_color_red_preference
            response["hair_color_red_preference"] = "updated"

        if growth_preference == preferences.growth_preference:
            response["growth_preference"] = "no changes"
        else:
            preferences.growth_preference = growth_preference
            response["growth_preference"] = "updated"

        if weight_preference == preferences.weight_preference:
            response["weight_preference"] = "no changes"
        else:
            preferences.weight_preference = weight_preference
            response["weight_preference"] = "updated"

        if body_type_preference == preferences.body_type_preference:
            response["body_type_preference"] = "no changes"
        else:
            preferences.body_type_preference = body_type_preference
            response["body_type_preference"] = "updated"

        if is_smoking_preference == preferences.is_smoking_preference:
            response["is_smoking_preference"] = "no changes"
        else:
            preferences.is_smoking_preference = is_smoking_preference
            response["is_smoking_preference"] = "updated"

        if is_drinking_alcohol_preference == preferences.is_drinking_alcohol_preference:
            response["is_drinking_alcohol_preference"] = "no changes"
        else:
            preferences.is_drinking_alcohol_preference = is_drinking_alcohol_preference
            response["is_drinking_alcohol_preference"] = "updated"

        if response:
            preferences.save()
            account.save()
            return Response(response, status=status.HTTP_200_OK)
        else:
            response["detail"] = "request must contain user data"
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request):
        try:
            preferences = request.user.preferences
        except Preferences.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserPreferencesSerializer(preferences)
        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class SettingsView(APIView):
    @staticmethod
    def patch(request):
        try:
            account = request.user
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            settings = request.user.settings
        except Settings.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        response = {}

        dark_theme = request.data.get('dark_theme', False)

        if dark_theme == settings.dark_theme:
            response["dark_theme"] = "no changes"
        else:
            settings.dark_theme = dark_theme
            response["dark_theme"] = "updated"

        if response:
            settings.save()
            account.save()
            return Response(response, status=status.HTTP_200_OK)
        else:
            response["detail"] = "request must contain user data"
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request):
        try:
            settings = request.user.settings
        except Settings.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSettingsSerializer(settings)
        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class UserProfilePic(APIView):
    @staticmethod
    def get(request):
        try:
            account = request.user
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserProfilePicSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def patch(request):
        try:
            account = request.user
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        response = {}

        file = request.data.get('profile_picture', None)

        if not file:
            response["detail"] = "request must contain user data"
            stat = status.HTTP_400_BAD_REQUEST
        else:
            main, sub = file.content_type.split('/')
            if not (sub in ['jpeg', 'jpg', 'png']):
                response["detail"] = "wrong data type"
                stat = status.HTTP_400_BAD_REQUEST
            else:
                account.profile_picture = file
                response["detail"] = "photo added successfully"
                account.save()
                stat = status.HTTP_200_OK

        return Response(response, status=stat)

    @staticmethod
    def delete(request):
        # TODO: DELETE PHOTO
        return Response(status=status.HTTP_404_NOT_FOUND)
    # USER LIST - SEARCHER


@permission_classes([IsAuthenticated])
class UserListView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['name', 'surname', 'birthday', 'sex', 'location',
                     'hair_color', 'body_type', 'is_smoking',
                     'is_drinking_alcohol']
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.exclude(pk=request.user.pk)

        name = request.query_params.get('name', None)
        surname = request.query_params.get('surname', None)
        location = request.query_params.get('location', None)
        sex = request.query_params.get('sex', None)
        hair_color = request.query_params.get('hair_color', None)
        growth = request.query_params.get('growth', None)
        weight = request.query_params.get('weight', None)
        body_type = request.query_params.get('body_type', None)
        is_smoking = request.query_params.get('is_smoking', None)
        is_drinking_alcohol = request.query_params.get('is_drinking_alcohol', None)

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
        if not (is_smoking is None or is_smoking == ''):
            queryset = queryset.filter(is_smoking=is_smoking)
        if not (is_drinking_alcohol is None or is_drinking_alcohol == ''):
            queryset = queryset.filter(is_drinking_alcohol=is_drinking_alcohol)

        serializer = UserSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

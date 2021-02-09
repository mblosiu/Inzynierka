import random
import string

from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.db.models import Lookup, Field, Q
from django.shortcuts import get_list_or_404
from django.template.loader import render_to_string
from rest_framework import status, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegistrationSerializer, UserSerializer, UserPreferencesSerializer, UserProfilePicSerializer, \
    UserSettingsSerializer, ImageSerializer, LikesSerializer, BlackListSerializer, FriendListSerializer, \
    ReportSerializer
from ..models import User, Image, Like, BlackList, Friend, Report, Verify

EMAIL_SENDER = 'noreply.elove@gmail.com'


def password_generator(length):
    printable = f'{string.ascii_letters}{string.digits}'

    printable = list(printable)
    random.shuffle(printable)

    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)
    return random_password


@Field.register_lookup
class NotEqual(Lookup):
    lookup_name = 'ne'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return '%s <> %s' % (lhs, rhs), params


# wysyła maila przy rejestracji
@permission_classes([])
class RegistrationView(APIView):
    @staticmethod
    def post(request):
        serializer = RegistrationSerializer(data=request.data)

        data = {}
        if not serializer.is_valid():
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(request)

        data['detail'] = 'successfully registered new user.'

        user = get_object_or_404(User, username=request.data.get("username"))
        verify_code = password_generator(32)

        while Verify.objects.filter(verify_code=verify_code).count() > 0:
            verify_code = password_generator(32)

        verify = Verify(
            user=user,
            verify_code=verify_code
        )
        verify.save()

        msg_html = render_to_string('mail/registration.html',
                                    {'username': serializer.data.get("username"),
                                     'verify_code': verify_code})
        msg_plain = render_to_string('mail/registration.txt',
                                     {'username': serializer.data.get("username"),
                                      'verify_code': verify_code})
        send_mail("[elove.ml] Rejestracja konta", msg_plain, EMAIL_SENDER, [serializer.data.get("email")],
                  fail_silently=False,
                  html_message=msg_html)

        return Response(data, status=status.HTTP_201_CREATED)


@permission_classes([])
class RegistrationValidationView(APIView):
    @staticmethod
    def get(request):
        username = request.data.get('username', None)
        print(username)
        email = request.data.get('email', None)
        data = {}

        if (username is None or username == '') and (email is None or email == ''):
            return Response({"detail": "You sent no data to check"}, status=status.HTTP_400_BAD_REQUEST)

        if username is not None and username != '':
            user_username = User.objects.filter(username=username)

            if user_username.count() > 0:
                data['username'] = "username in use"
            else:
                data['username'] = "username is free to use"

        if email is not None and email != '':
            user_email = User.objects.filter(email=email)

            if user_email.count() > 0:
                data['email'] = "email in use"
            else:
                data['email'] = "email is free to use"

        return Response(data, status=status.HTTP_200_OK)


# po kliknięciu w mailu weryfikuje konto
@permission_classes([])
class VerifyAccountView(APIView):
    @staticmethod
    def patch(request):
        verify_code = request.data.get('verify_code')
        verify_object = get_object_or_404(Verify, verify_code=verify_code)
        user = verify_object.user

        if user.verified:
            return Response({'detail': 'already verified'}, status=status.HTTP_400_BAD_REQUEST)

        if verify_object.verify_code != verify_code:
            return Response({'detail': 'wrong verify code'}, status=status.HTTP_401_UNAUTHORIZED)

        user.verified = True
        user.save()

        return Response({'detail': 'account verified successfully'}, status=status.HTTP_200_OK)


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
        password = request.data.get('password')

        if not request.user.check_password(password):
            return Response({"detail": "wrong password"}, status=status.HTTP_400_BAD_REQUEST)

        if request.user.delete():
            return Response({"detail": "Account removed successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "error"}, status=status.HTTP_400_BAD_REQUEST)


# zmień hasło
@permission_classes([IsAuthenticated])
class ChangePasswordView(APIView):
    @staticmethod
    def patch(request):
        user = get_object_or_404(User, pk=request.user.pk)

        password = request.data.get('password')
        new_password1 = request.data.get('new_password1')
        new_password2 = request.data.get('new_password2')

        if not user.check_password(password):
            return Response({'detail': 'wrong current password'}, status=status.HTTP_400_BAD_REQUEST)

        if not new_password1 == new_password2:
            return Response({'detail': 'passwords does not match'}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password1)
        user.save()

        msg_html = render_to_string('mail/change_password.html', {'username': user.username})
        msg_plain = render_to_string('mail/change_password.txt', {'username': user.username})

        send_mail("[elove.ml] Zmiana hasła", msg_plain, EMAIL_SENDER, [user.email], fail_silently=False,
                  html_message=msg_html)

        return Response({'detail': 'password changed'}, status=status.HTTP_200_OK)


# zmień hasło i wyślij na maila
@permission_classes([])
class RestorePasswordView(APIView):
    @staticmethod
    def patch(request):
        email = request.data.get('email')
        user = get_object_or_404(User, email=email)

        new_password = password_generator(8)
        user.set_password(new_password)

        user.save()

        msg_html = render_to_string('mail/restore_password.html', {'username': user.username, 'password': new_password})
        msg_plain = render_to_string('mail/restore_password.txt', {'username': user.username, 'password': new_password})
        send_mail("[elove.ml] Odzyskiwanie hasła", msg_plain, EMAIL_SENDER, [user.email], fail_silently=False,
                  html_message=msg_html)

        return Response({'detail': 'password changed'}, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class UserProfileView(APIView):
    @staticmethod
    def get(request):
        try:
            account = request.user
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def patch(request):
        try:
            account = request.user
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        response = {}

        email = request.data.get('email', None)
        name = request.data.get('name', None)
        surname = request.data.get('surname', None)
        location = request.data.get('location', None)
        sex = request.data.get('sex', None)
        hair_color = request.data.get('hair_color', None)
        body_type = request.data.get('body_type', None)
        growth = request.data.get('growth', None)
        weight = request.data.get('weight', None)
        description = request.data.get('description', None)
        is_smoking = request.data.get('is_smoking', None)
        is_drinking_alcohol = request.data.get('is_drinking_alcohol', None)
        orientation = request.data.get('orientation', None)
        eye_color = request.data.get('eye_color', None)
        hair_length = request.data.get('hair_length', None)
        status1 = request.data.get('status', None)
        education = request.data.get('education', None)

        if email in [None, '', account.email]:
            response["email"] = "no changes"
        else:
            userlist = User.objects.filter(email=email)
            if userlist:
                response["email"] = "This email is occupied"
            else:
                account.email = email
                response["email"] = "updated"

        if name == account.name or name is None:
            response["name"] = "no changes"
        else:
            account.name = name.capitalize()
            response["name"] = "updated"

        if surname == account.surname or surname is None:
            response["surname"] = "no changes"
        else:
            account.surname = surname.capitalize()
            response["surname"] = "updated"

        if location == account.location or location is None:
            response["location"] = "no changes"
        else:
            account.location = location.capitalize()
            response["location"] = "updated"

        if sex == account.sex or sex is None:
            response["sex"] = "no changes"
        else:
            account.sex = sex.capitalize()
            response["sex"] = "updated"

        if orientation == account.orientation or orientation is None:
            response["orientation"] = "no changes"
        else:
            account.orientation = orientation.capitalize()
            response["orientation"] = "updated"

        if status1 == account.status or status1 is None:
            response["status"] = "no changes"
        else:
            account.status = status1.capitalize()
            response["status"] = "updated"

        if education == account.education or education is None:
            response["education"] = "no changes"
        else:
            account.education = education.capitalize()
            response["education"] = "updated"

        if hair_length == account.hair_length or hair_length is None:
            response["hair_length"] = "no changes"
        else:
            account.hair_length = hair_length
            response["hair_length"] = "updated"

        if eye_color == account.eye_color or eye_color is None:
            response["eye_color"] = "no changes"
        else:
            account.eye_color = eye_color.capitalize()
            response["eye_color"] = "updated"

        if hair_color == account.hair_color or hair_color is None:
            response["hair_color"] = "no changes"
        else:
            account.hair_color = hair_color.capitalize()
            response["hair_color"] = "updated"

        if growth == account.growth or growth is None:
            response["growth"] = "no changes"
        else:
            account.growth = growth
            response["growth"] = "updated"

        if weight == account.weight or weight is None:
            response["weight"] = "no changes"
        else:
            account.weight = weight
            response["weight"] = "updated"

        if body_type == account.body_type or body_type is None:
            response["body_type"] = "no changes"
        else:
            account.body_type = body_type.capitalize()
            response["body_type"] = "updated"

        if is_smoking == account.is_smoking or is_smoking is None:
            response["is_smoking"] = "no changes"
        else:
            if is_smoking.isdecimal():
                account.is_smoking = int(is_smoking)
                response["is_smoking"] = "updated"
            else:
                response["is_smoking"] = "no changes"

        if is_drinking_alcohol == account.is_drinking_alcohol or is_drinking_alcohol is None:
            response["is_drinking_alcohol"] = "no changes"
        else:
            if is_drinking_alcohol.isdecimal():
                account.is_drinking_alcohol = int(is_drinking_alcohol)
                response["is_drinking_alcohol"] = "updated"
            else:
                account.is_drinking_alcohol = int(is_drinking_alcohol)
                response["is_drinking_alcohol"] = "no changes"

        if description == account.description or description is None:
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
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            preferences = request.user.preferences
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        response = {}

        hair_color_blonde_preference = request.data.get('hair_color_blonde_preference', None)
        hair_color_brunette_preference = request.data.get('hair_color_brunette_preference', None)
        hair_color_red_preference = request.data.get('hair_color_red_preference', None)
        growth_preference = request.data.get('growth_preference', None)
        weight_preference = request.data.get('weight_preference', None)
        body_type_preference = request.data.get('body_type_preference', None)
        is_smoking_preference = request.data.get('is_smoking_preference', None)
        is_drinking_alcohol_preference = request.data.get('is_drinking_alcohol_preference', None)
        age_preference_min = request.data.get('age_preference_min', None)
        age_preference_max = request.data.get('age_preference_max', None)

        if age_preference_min == str(preferences.age_preference_min) or age_preference_min is None:
            response["age_preference_min"] = "no changes"
        else:
            preferences.age_preference_min = int(age_preference_min)
            response["age_preference_min"] = "updated"

        if age_preference_max == str(preferences.age_preference_max) or age_preference_max is None:
            response["age_preference_max"] = "no changes"
        else:
            preferences.age_preference_max = int(age_preference_max)
            response["age_preference_max"] = "updated"

        if hair_color_blonde_preference == preferences.hair_color_blonde_preference or hair_color_blonde_preference is None:
            response["hair_color_blonde_preference"] = "no changes"
        else:
            preferences.hair_color_blonde_preference = hair_color_blonde_preference.capitalize()
            response["hair_color_blonde_preference"] = "updated"

        if hair_color_brunette_preference == preferences.hair_color_brunette_preference or hair_color_brunette_preference is None:
            response["hair_color_brunette_preference"] = "no changes"
        else:
            preferences.hair_color_brunette_preference = hair_color_brunette_preference.capitalize()
            response["hair_color_brunette_preference"] = "updated"

        if hair_color_red_preference == preferences.hair_color_red_preference or hair_color_red_preference is None:
            response["hair_color_red_preference"] = "no changes"
        else:
            preferences.hair_color_red_preference = hair_color_red_preference.capitalize()
            response["hair_color_red_preference"] = "updated"

        if growth_preference == preferences.growth_preference or growth_preference is None:
            response["growth_preference"] = "no changes"
        else:
            preferences.growth_preference = growth_preference
            response["growth_preference"] = "updated"

        if weight_preference == preferences.weight_preference or weight_preference is None:
            response["weight_preference"] = "no changes"
        else:
            preferences.weight_preference = weight_preference
            response["weight_preference"] = "updated"

        if body_type_preference == preferences.body_type_preference or body_type_preference is None:
            response["body_type_preference"] = "no changes"
        else:
            preferences.body_type_preference = body_type_preference.capitalize()
            response["body_type_preference"] = "updated"

        if is_smoking_preference == preferences.is_smoking_preference or is_smoking_preference is None:
            response["is_smoking_preference"] = "no changes"
        else:
            preferences.is_smoking_preference = is_smoking_preference.capitalize()
            response["is_smoking_preference"] = "updated"

        if is_drinking_alcohol_preference == preferences.is_drinking_alcohol_preference or is_drinking_alcohol_preference is None:
            response["is_drinking_alcohol_preference"] = "no changes"
        else:
            preferences.is_drinking_alcohol_preference = is_drinking_alcohol_preference.capitalize()
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
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserPreferencesSerializer(preferences)
        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class SettingsView(APIView):
    @staticmethod
    def patch(request):
        try:
            account = request.user
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            settings = request.user.settings
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        response = {}
        dark_theme = request.data.get('dark_theme', None)
        messages_privacy = request.data.get('messages_privacy', None)
        search_privacy = request.data.get('search_privacy', None)
        comments_privacy = request.data.get('comments_privacy', None)
        hide_age = request.data.get('hide_age', None)

        if dark_theme == settings.dark_theme or dark_theme is None:
            response["dark_theme"] = "no changes"
        else:
            settings.dark_theme = dark_theme
            response["dark_theme"] = "updated"

        if messages_privacy == settings.messages_privacy or messages_privacy is None:
            response["messages_privacy"] = "no changes"
        else:
            settings.messages_privacy = messages_privacy
            response["messages_privacy"] = "updated"

        if search_privacy == settings.search_privacy or search_privacy is None:
            response["search_privacy"] = "no changes"
        else:
            settings.search_privacy = search_privacy
            response["search_privacy"] = "updated"

        if comments_privacy == settings.comments_privacy or comments_privacy is None:
            response["comments_privacy"] = "no changes"
        else:
            settings.comments_privacy = comments_privacy
            response["comments_privacy"] = "updated"

        if hide_age == settings.hide_age or hide_age is None:
            response["hide_age"] = "no changes"
        else:
            settings.hide_age = hide_age
            response["hide_age"] = "updated"

        settings.save()
        account.save()
        return Response(response, status=status.HTTP_200_OK)

    @staticmethod
    def get(request):
        try:
            settings = request.user.settings
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSettingsSerializer(settings)
        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class UserProfilePic(APIView):
    @staticmethod
    def patch(request):
        try:
            account = request.user
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        response = {}

        profile_picture = request.data.get('profile_picture', None)

        if profile_picture == account.profile_picture or profile_picture is None:
            response["profile_picture"] = "no changes"
        else:
            account.profile_picture = profile_picture
            response["profile_picture"] = "updated"

        if response:
            account.save()
            return Response(response, status=status.HTTP_200_OK)
        else:
            response["detail"] = "request must contain user data"
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request):
        try:
            user = request.user
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserProfilePicSerializer(user.profile_picture)
        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class UserImage(APIView):
    @staticmethod
    def get(request):
        try:
            user = request.user
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        images = Image.objects.filter(user__pk=user.pk)

        serializer = ImageSerializer(images, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        try:
            user = request.user
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        file = request.data.get('image', None)

        if not file:
            return Response({"detail": "request must contain image"}, status=status.HTTP_400_BAD_REQUEST)

        main, sub = file.content_type.split('/')

        if not (sub in ['jpeg', 'jpg', 'png']):
            return Response({"detail": "wrong data type"}, status=status.HTTP_400_BAD_REQUEST)

        image = Image(
            user=user,
            image=file,
            title=main,
            alt=main,
        )
        image.save()
        return Response({"detail": "photo added successfully"}, status=status.HTTP_201_CREATED)

    @staticmethod
    def delete(request):
        try:
            user = request.user
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        pk = request.data.get('pk', None)
        # image = Image.objects.filter(pk=pk, user__pk=user.pk)
        image = get_object_or_404(Image, pk=pk, user__pk=user.pk)
        image.delete()
        return Response({"detail": "Image removed successfully"}, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class ImageByUserId(APIView):
    @staticmethod
    def get(request, pk=None):
        images = Image.objects.filter(user__pk=pk)

        serializer = ImageSerializer(images, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


# USER LIST - SEARCHER
@permission_classes([IsAuthenticated])
class UserListView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['username', 'name', 'surname', 'birthday', 'sex', 'location',
                     'hair_color', 'body_type', 'is_smoking',
                     'is_drinking_alcohol']
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        # nie można wyszukać samego siebie
        queryset = queryset.exclude(pk=request.user.pk)

        # jeżeli user ma zablokowaną widoczność profilu
        queryset = queryset.exclude(settings__search_privacy='nobody')

        # jeżeli user ma ustawione friends only
        friendlist = Friend.objects.filter(user__pk=request.user.pk).values_list("friend", flat=True)
        queryset = queryset.exclude(~Q(pk__in=friendlist), settings__search_privacy="friends")

        # jeżeli user chce być wyświetlany tylko przez inną płeć
        queryset = queryset.exclude(settings__search_privacy='diffrent_sex', sex__ne=request.user.sex)

        # jeżeli user jest na mojej black liście to go nie widzę
        blacklist = BlackList.objects.filter(user__pk=request.user.pk).values_list("blacklisted", flat=True)
        queryset = queryset.exclude(pk__in=blacklist)

        # jeżeli user mnie zablokował to ja go nie widzę
        blacklist = BlackList.objects.filter(blacklisted__pk=request.user.pk).values_list("user", flat=True)
        queryset = queryset.exclude(pk__in=blacklist)

        name = request.query_params.get('name', None)
        surname = request.query_params.get('surname', None)
        sex = request.query_params.get('sex', None)
        location = request.query_params.get('location', None)
        hair_length = request.query_params.get('hair_length', None)
        hair_color = request.query_params.get('hair_color', None)
        growth = request.query_params.get('growth', None)
        body_type = request.query_params.get('body_type', None)
        is_smoking = request.query_params.get('is_smoking', None)
        is_drinking_alcohol = request.query_params.get('is_drinking_alcohol', None)
        orientation = request.query_params.get('orientation', None)
        eye_color = request.query_params.get('eye_color', None)
        age_preference_min = request.query_params.get('age_preference_min', None)
        age_preference_max = request.query_params.get('age_preference_max', None)

        if not (location is None or location == ''):
            queryset = queryset.filter(location=location.capitalize())
        if not (sex is None or sex == ''):
            queryset = queryset.filter(sex=sex.capitalize())
        if not (orientation is None or orientation == ''):
            queryset = queryset.filter(orientation=orientation.capitalize())
        if not (age_preference_min is None or age_preference_min == ''):
            queryset = queryset.filter(age__gte=int(age_preference_min))
        if not (age_preference_max is None or age_preference_max == ''):
            queryset = queryset.filter(age__lte=int(age_preference_max))
        if not (eye_color is None or eye_color == ''):
            queryset = queryset.filter(eye_color=eye_color.capitalize())
        if not (name is None or name == ''):
            queryset = queryset.filter(name=name.capitalize())
        if not (surname is None or surname == ''):
            queryset = queryset.filter(surname=surname.capitalize())
        if not (hair_color is None or hair_color == ''):
            queryset = queryset.filter(hair_color=hair_color.capitalize())
        if not (growth is None or growth == ''):
            queryset = queryset.filter(growth=growth)
        if not (hair_length is None or hair_length == ''):
            queryset = queryset.filter(hair_length=hair_length)
        if not (body_type is None or body_type == ''):
            queryset = queryset.filter(body_type=body_type.capitalize())
        if not (is_smoking is None or is_smoking == ''):
            if is_smoking.isdecimal():
                queryset = queryset.filter(is_smoking__lte=int(is_smoking))
        if not (is_drinking_alcohol is None or is_drinking_alcohol == ''):
            if is_drinking_alcohol.isdecimal():
                queryset = queryset.filter(is_drinking_alcohol__lte=int(is_drinking_alcohol))
        serializer = UserSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class RandomPair(APIView):
    @staticmethod
    def get(request):
        queryset = User.objects.all()
        # nie można wyszukać samego siebie
        queryset = queryset.exclude(pk=request.user.pk)

        # todo: sprawdzić czy działa
        # blokuje userów uprzednio odrzuconych lub polubionych
        likes = Like.objects.filter(pk=request.user.pk).values_list("liked", flat=True)
        queryset = queryset.exclude(pk__in=likes)

        # jeżeli user ma zablokowaną widoczność profilu
        queryset = queryset.exclude(settings__search_privacy='nobody')

        # jeżeli user chce być wyświetlany tylko przez płeć przeciwną
        queryset = queryset.exclude(settings__search_privacy='diffrent sex', sex__ne=request.user.sex)

        # jeżeli user chce być wyświetlany tylko przez taką samą płeć
        queryset = queryset.exclude(settings__search_privacy='same sex', sex=request.user.sex)

        # jeżeli user ma ustawione friends only
        friendlist = Friend.objects.filter(user__pk=request.user.pk).values_list("friend", flat=True)
        queryset = queryset.exclude(~Q(pk__in=friendlist), settings__search_privacy="friends")

        # jeżeli user jest na mojej black liście to go nie widzę
        blacklist = BlackList.objects.filter(user__pk=request.user.pk).values_list("blacklisted", flat=True)
        queryset = queryset.exclude(pk__in=blacklist)

        # jeżeli user mnie zablokował to ja go nie widzę
        blacklist = BlackList.objects.filter(blacklisted__pk=request.user.pk).values_list("user", flat=True)
        queryset = queryset.exclude(pk__in=blacklist)

        # todo: filters

        orientation = request.user.orientation
        hair_color_blonde_preference = request.user.preferences.hair_color_blonde_preference
        hair_color_brunette_preference = request.user.preferences.hair_color_brunette_preference
        hair_color_red_preference = request.user.preferences.hair_color_red_preference
        growth_preference = request.user.preferences.growth_preference
        weight_preference = request.user.preferences.weight_preference
        body_type_preference = request.user.preferences.body_type_preference
        freckles_preference = request.user.preferences.freckles_preference
        glasses_preference = request.user.preferences.glasses_preference
        hair_length_preference = request.user.preferences.hair_length_preference
        is_smoking_preference = request.user.preferences.is_smoking_preference
        is_drinking_alcohol_preference = request.user.preferences.is_drinking_alcohol_preference
        age_preference_min = request.user.preferences.age_preference_min
        age_preference_max = request.user.preferences.age_preference_max

        if not (age_preference_min is None or age_preference_min == ''):
            if age_preference_min.isdecimal():
                queryset = queryset.filter(age__gte=int(age_preference_min))

        if not (age_preference_max is None or age_preference_max == ''):
            if age_preference_min.isdecimal():
                queryset = queryset.filter(age__lte=int(age_preference_max))

        if not (is_smoking_preference is None or is_smoking_preference == ''):
            if is_smoking_preference.isdecimal():
                queryset = queryset.filter(is_smoking__lte=int(is_smoking_preference))

        if not (is_drinking_alcohol_preference is None or is_drinking_alcohol_preference == ''):
            if is_drinking_alcohol_preference.isdecimal():
                queryset = queryset.filter(is_drinking_alcohol__lte=int(is_drinking_alcohol_preference))

        x = random.randint(0, queryset.count() - 1)

        serializer = UserSerializer(queryset[x])

        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([])
class ValidUsernameAndEmail(APIView):
    @staticmethod
    def post(request):
        email = request.data.get('email', None)
        username = request.data.get('username', None)

        queryset = User.objects.filter(email=email)
        queryset2 = User.objects.filter(username=username)

        response = {}
        print(queryset.count())
        if queryset.count() > 0:
            response["email"] = "exists"
        else:
            response["email"] = "valid"

        if queryset2.count() > 0:
            response["username"] = "exists"
        else:
            response["username"] = "valid"

        return Response(response, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class LikesView(viewsets.ModelViewSet):
    serializer_class = LikesSerializer
    queryset = Like.objects.all()

    # zostałeś polubiony
    @staticmethod
    def create_like(request):
        value = request.data.get('value', None)
        pk = request.data.get('pk', None)

        current_user = get_object_or_404(User, pk=pk)
        user = get_object_or_404(User, pk=request.user.pk)
        response = {}
        if value in ['like', 'dislike']:
            like = Like(
                value=value,
                liked=user,
                liked_by=current_user
            )
            like.save()
            response["detail"] = "success"
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response["detail"] = "failed"
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete_like(request):
        pk = request.data.get('pk', None)

        if get_object_or_404(Like, pk=pk).delete():
            return Response({"detail": "Like removed successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "invalid token"}, status=status.HTTP_400_BAD_REQUEST)

    # kogo polubił user po pk - userprofile
    @staticmethod
    def get_liked_users(request, pk=None):
        queryset = Like.objects.filter(liked_by__pk=pk)
        serializer = LikesSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # lajki użytkownika po pk - userprofile
    @staticmethod
    def get_like_users(request, pk=None):
        queryset = Like.objects.filter(liked__pk=pk)
        serializer = LikesSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # kogo polubił user po pk - mainuser
    @staticmethod
    def get_liked_user(request):
        pk = request.user.pk
        queryset = Like.objects.filter(liked_by__pk=pk)
        serializer = LikesSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # lajki użytkownika po pk - mainuser
    @staticmethod
    def get_like_user(request):
        pk = request.user.pk
        queryset = Like.objects.filter(liked__pk=pk)
        serializer = LikesSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class BlackListView(APIView):
    @staticmethod
    def post(request):
        response = {}
        pk = request.data.get('pk', None)

        if int(pk) == int(request.user.pk):
            return Response({"detail": "can't block yourself"}, status=status.HTTP_400_BAD_REQUEST)
        blacklist = BlackList.objects.filter(user=request.user.pk, blacklisted=pk)

        if blacklist.count() > 0:
            response["detail"] = "already blocked"
            stat = status.HTTP_400_BAD_REQUEST
        else:
            response["detail"] = "user blocked"
            blacklist = BlackList(
                user=request.user,
                blacklisted=get_object_or_404(User, pk=pk)
            )
            blacklist.save()
            stat = status.HTTP_201_CREATED
        return Response(response, status=stat)

    @staticmethod
    def delete(request):
        pk = request.data.get('pk', None)
        blacklist = get_object_or_404(BlackList, user__pk=request.user.pk, blacklisted__pk=pk)

        if blacklist.delete():
            return Response({"detail": "success"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "invalid token"}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request):
        pk = request.query_params.get('pk', None)
        queryset = get_list_or_404(BlackList, user__pk=pk)
        serializer = BlackListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class FriendListView(APIView):
    @staticmethod
    def post(request):
        response = {}
        pk = request.data.get('pk', None)

        if int(pk) == int(request.user.pk):
            return Response({"detail": "can't add to contacts yourself"}, status=status.HTTP_400_BAD_REQUEST)

        friendlist1 = Friend.objects.filter(user=request.user.pk, friend=pk)
        friendlist2 = Friend.objects.filter(user=pk, friend=request.user.pk)

        if friendlist1.count() > 0 or friendlist2.count() > 0:
            response["detail"] = "already on friendlist"
            stat = status.HTTP_400_BAD_REQUEST
        else:
            response["detail"] = "user added to friendlist"
            friendlist1 = Friend(
                status='waiting',
                user=request.user,
                friend=get_object_or_404(User, pk=pk),
            )
            friendlist2 = Friend(
                status='waiting for your accept',
                user=get_object_or_404(User, pk=pk),
                friend=request.user,
            )
            friendlist1.save()
            friendlist2.save()
            stat = status.HTTP_201_CREATED

        return Response(response, status=stat)

    @staticmethod
    def patch(request):
        pk = request.data.get("pk")

        friendlist1 = get_object_or_404(Friend, user__pk=request.user.pk, friend__pk=pk,
                                        status="waiting for your accept")
        friendlist2 = get_object_or_404(Friend, user__pk=pk, friend__pk=request.user.pk, status='waiting')

        stat = status.HTTP_200_OK
        response = {"detail": "success"}

        friendlist1.status = "accepted"
        friendlist2.status = "accepted"
        friendlist1.save()
        friendlist2.save()

        return Response(response, status=stat)

    @staticmethod
    def delete(request):
        pk = request.data.get('pk', None)

        friendlist1 = get_object_or_404(Friend, user__pk=request.user.pk, friend__pk=pk)

        friendlist2 = get_object_or_404(Friend, user__pk=pk, friend__pk=request.user.pk)

        if friendlist1.delete() and friendlist2.delete():
            return Response({"detail": "success"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "error"}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request):
        pk = request.query_params.get('pk', None)

        queryset = Friend.objects.filter(user__pk=pk)

        serializer = FriendListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class ReportView(APIView):
    @staticmethod
    def post(request):
        reporting = request.user
        reported = request.data.get('reported', None)
        reason = request.data.get('reason', None)
        description = request.data.get('description', None)
        status_ = "new"

        if reported is not None and reported != '':
            reported = get_object_or_404(User, pk=reported)
        else:
            reported = None

        if reporting is None or reporting == '' or reason is None or reason == '' or reporting == reported:
            return Response({"detail": "wrong data"}, status=status.HTTP_400_BAD_REQUEST)

        report = Report(
            reporting=reporting,
            reported=reported,
            reason=reason,
            description=description,
            status=status_
        )

        report.save()

        return Response({"detail": "report sent successfully"}, status=status.HTTP_201_CREATED)

    @staticmethod
    def delete(request):
        pk = request.data.get('pk', None)
        reporting = request.data.get('reporting_pk', None)
        reported = request.data.get('reported_pk', None)
        if pk is not None and pk != '':
            report = get_object_or_404(Report, pk=pk)
        elif reporting is not None and reporting != '' and reported is not None and reported != '':
            report = get_object_or_404(Report, reporting__pk=reporting, reported__pk=reported)
        else:
            return Response({"detail": "wrong data"}, status=status.HTTP_400_BAD_REQUEST)

        if report.delete():
            return Response({"detail": "success"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "error"}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request):
        pk = request.user.pk
        queryset = get_list_or_404(Report, reporting__pk=pk)
        serializer = ReportSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([IsAdminUser])
class AdminReportView(APIView):
    @staticmethod
    def patch(request):
        pk = request.data.get('pk', None)
        status_ = request.data.get('status', None)

        report = get_object_or_404(Report, pk=pk)

        report.status = status_

        return Response({"detail": "status changed successfully"}, status=status.HTTP_200_OK)

    @staticmethod
    def delete(request):
        pk = request.data.get('pk', None)

        if pk is not None and pk != '':
            report = get_object_or_404(Report, pk=pk)
        else:
            return Response({"detail": "wrong data"}, status=status.HTTP_400_BAD_REQUEST)

        if report.delete():
            return Response({"detail": "success"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "error"}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request):
        queryset = get_list_or_404(Report)
        serializer = ReportSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([])
class TemplateSendMail(APIView):
    def post(self, request):
        email = request.data.get("email")

        msg_plain = render_to_string('mail/test/test.html', {'some_params': 'param'})
        msg_html = render_to_string('mail/test/test.html', {'some_params': 'param'})

        send_mail("subject", msg_plain, EMAIL_SENDER, [email], fail_silently=False, html_message=msg_html)

        return Response({'detail': 'success'}, status=status.HTTP_200_OK)

# ctrl + alt + O - formatowanie importów
# ctrl + alt + L - formatowanie kodu
# ctrl + shift + - - zwiń wszystko

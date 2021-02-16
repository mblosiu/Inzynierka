import random
import string
from datetime import datetime, timedelta, timezone, date

from rest_framework import serializers

from ..models import User, Preferences, Settings, Image, Like, BlackList, Friend, Report, Verify, BannedIp


class UserPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preferences
        fields = ['hair_color_blonde_preference', 'hair_color_brunette_preference',
                  'hair_color_red_preference', 'growth_preference', 'weight_preference', 'body_type_preference',
                  'is_smoking_preference', 'is_drinking_alcohol_preference', 'age_preference_max', 'age_preference_min']


class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ['dark_theme', 'messages_privacy', 'search_privacy', 'comments_privacy', 'hide_age']


class UserSerializer(serializers.ModelSerializer):
    preferences = UserPreferencesSerializer(read_only=True)
    settings = UserSettingsSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['pk', 'email', 'username', 'last_login', 'is_active', 'name', 'surname', 'birthday', 'location',
                  'profile_picture', 'description', 'sex', 'hair_color', 'hair_length', 'growth', 'weight', 'body_type',
                  'freckles', 'glasses', 'is_smoking', 'is_drinking_alcohol', 'eye_color', 'education', 'passion',
                  'favourite_place', 'status', 'orientation', 'preferences', 'settings'
                  ]


class UserProfilePicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['profile_picture']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['pk', 'image', 'title', 'alt']


class UserCheck(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'ip', 'date_joined']


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'location', 'birthday', 'sex', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self, request):
        client_ip = request.META['REMOTE_ADDR']
        username = self.validated_data.get('username')
        email = self.validated_data.get('email')
        location = self.validated_data.get('location')
        birthday = self.validated_data.get('birthday')
        sex = self.validated_data.get('sex')
        verified = False

        password = self.validated_data.get('password')
        password2 = self.validated_data.get('password2')

        # hasło wymaga 8 znaków
        if len(password) < 8:
            raise serializers.ValidationError({'detail': ["password must contain 8 characters"]})

        # whitelist ip
        if client_ip not in ['77.65.82.115', '37.247.57.187']:
            # limit 10 kont na ip
            account_list = User.objects.filter(ip=client_ip)
            if account_list.count() >= 10:
                raise serializers.ValidationError({'detail': ["you can't create more accounts"]})

            # sprawdza czy zbanowany
            banned_list = BannedIp.objects.filter(ip=client_ip)
            if banned_list.count() > 0:
                raise serializers.ValidationError({'detail': ['you have been permanently banned']})

            # blokowanie spamerskiego tworzenia kont
            time = datetime.now(timezone.utc) - timedelta(seconds=5)
            account_list = User.objects.filter(ip=client_ip, date_joined__gt=time)
            if account_list.count() >= 1:
                banned_ip = BannedIp(ip=client_ip)
                banned_ip.save()

                for acc in account_list:
                    acc.account_status = "banned"
                    acc.save()
                raise serializers.ValidationError({'detail': ["you have been permanently banned"]})
        else:
            verified = True
        # testowy fix 500
        if client_ip is None:
            raise serializers.ValidationError({'client_ip': ['Something went wrong.']})
        if username is None:
            raise serializers.ValidationError({'username': ['This field is required.']})
        elif email is None:
            raise serializers.ValidationError({'email': ['This field is required.']})
        elif location is None:
            raise serializers.ValidationError({'location': ['This field is required.']})
        elif birthday is None:
            raise serializers.ValidationError({'birthday': ['This field is required.']})
        elif sex is None:
            raise serializers.ValidationError({'sex': ['This field is required.']})
        elif password is None:
            raise serializers.ValidationError({'password': 'This field is required.'})
        elif password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})

        today = date.today()
        age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

        if age < 18:
            raise serializers.ValidationError({'detail': 'You must be 18 years old to create an account'})

        p = Preferences()
        p.save()
        s = Settings(
            dark_theme=False,
        )
        s.save()
        account = User(
            username=username,
            email=email,
            location=location,
            birthday=birthday,
            sex=sex,
            preferences=p,
            settings=s,
            age=age,
            ip=client_ip,
            verified=verified,
        )
        account.set_password(password)
        account.save()

        return account


class LikesSerializer(serializers.ModelSerializer):
    liked = UserSerializer(read_only=True)
    liked_by = UserSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ['pk', 'value', 'liked', 'liked_by']


class BlackListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    blacklisted = UserSerializer(read_only=True)

    class Meta:
        model = BlackList
        fields = ['pk', 'user', 'blacklisted']


class FriendListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    friend = UserSerializer(read_only=True)

    class Meta:
        model = Friend
        fields = ['pk', 'status', 'user', 'friend']


class ReportSerializer(serializers.ModelSerializer):
    reporting = UserSerializer(read_only=True)
    reported = UserSerializer(read_only=True)

    class Meta:
        model = Report
        fields = ['pk', 'status', 'reporting', 'reported', 'reason', 'description']


class VerifyAccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Verify
        fields = ['pk', 'user', 'verify_code']

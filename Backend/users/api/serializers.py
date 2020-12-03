from datetime import datetime

from rest_framework import serializers

from ..models import User, Preferences, Settings, Image, Like, BlackList, FriendsList


class UserPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preferences
        fields = ['hair_color_blonde_preference', 'hair_color_brunette_preference',
                  'hair_color_red_preference', 'growth_preference', 'weight_preference', 'body_type_preference',
                  'is_smoking_preference', 'is_drinking_alcohol_preference', 'age_preference_max', 'age_preference_min']


class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ['dark_theme', 'messages_privacy', 'search_privacy', 'comments_privacy']


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


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'location', 'birthday', 'sex', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        username = self.validated_data.get('username')
        email = self.validated_data.get('email')
        location = self.validated_data.get('location')
        birthday = self.validated_data.get('birthday')
        sex = self.validated_data.get('sex')

        password = self.validated_data.get('password')
        password2 = self.validated_data.get('password2')

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
            age=int(datetime.today().strftime('%Y')) - int(birthday.strftime("%Y")),
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
        model = FriendsList
        fields = ['pk', 'status', 'user', 'friend']

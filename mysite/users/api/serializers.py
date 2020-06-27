from rest_framework import serializers
from ..models import Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'email', 'name', 'surname', 'birthday', 'sex', 'location', 'profile_picture',
                  'description', 'hair_color', 'growth', 'weight', 'body_type', 'race_origin', 'is_smoking',
                  'is_drinking_alcohol']


class UserProfilePicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['profile_picture']


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
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

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

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
        elif password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})

        account = Account(
            username=username,
            email=email,
            location=location,
            birthday=birthday,
            sex=sex,
        )
        account.set_password(password)
        account.save()
        return account

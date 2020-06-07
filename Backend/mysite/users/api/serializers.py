from rest_framework import serializers
from ..models import Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'email', 'name', 'surname', 'birthday', 'sex', 'location']


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['username', 'email', 'location', 'birthday', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        try:
            if self.validated_data['location'] is None:
                raise serializers.ValidationError({'location': ['This field is required.']})
        except KeyError:
            raise serializers.ValidationError({'location': ['This field is required.']})
        try:
            if self.validated_data['birthday'] is None:
                raise serializers.ValidationError({'birthday': ['This field is required.']})
        except KeyError:
            raise serializers.ValidationError({'birthday': ['This field is required.']})

        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        account = Account(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            location=self.validated_data['location'],
            birthday=self.validated_data['birthday'],
        )
        account.set_password(password)
        account.save()
        return account

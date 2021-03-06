from rest_framework import serializers
from users.api.serializers import UserSerializer

from ..models import Message


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['pk', 'created', 'sender', 'receiver', 'message']

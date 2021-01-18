import random
import string
from itertools import chain
from operator import attrgetter
from datetime import datetime
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

from users.models import User
from ..models import Message
from .serializers import MessageSerializer


@permission_classes([IsAuthenticated])
class ConversationView(APIView):
    @staticmethod
    def post(request, username):
        sender = request.user
        receiver = get_object_or_404(User, username=username)
        text_message = request.data.get("message")

        if request.user.username == username:
            return Response({"detail": "you can't chat with yourself"}, status=status.HTTP_400_BAD_REQUEST)

        if text_message is None or text_message == '':
            return Response({"detail": "no text message"}, status=status.HTTP_400_BAD_REQUEST)

        message = Message(sender=sender, receiver=receiver, message=text_message)
        message.save()

        return Response({"detail": "message sent successfully"}, status=status.HTTP_201_CREATED)

    @staticmethod
    def get(request, username):
        user = request.user
        interlocutor = get_object_or_404(User, username=username)
        if request.user.username == username:
            return Response({"detail": "you can't chat with yourself"}, status=status.HTTP_400_BAD_REQUEST)

        user_messages = Message.objects.filter(sender=user, receiver=interlocutor)
        interlocutor_messages = Message.objects.filter(sender=interlocutor, receiver=user)
        # user_messages_serializer = MessageSerializer(user_messages, many=True)
        # interlocutor_messages_serializer = MessageSerializer(interlocutor_messages, many=True)
        # response['user_messages'] = user_messages_serializer.data
        # response['interlocutor_messages'] = interlocutor_messages_serializer.data

        result_list = sorted(chain(user_messages, interlocutor_messages), key=attrgetter('created'))
        list_serializer = MessageSerializer(result_list, many=True)

        return Response({'detail': list_serializer.data}, status=status.HTTP_200_OK)

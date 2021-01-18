from itertools import chain
from operator import attrgetter

from rest_framework import status, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.models import User

from .serializers import MessageSerializer
from ..models import Message


@permission_classes([IsAuthenticated])
class ConversationView(viewsets.GenericViewSet):
    @staticmethod
    def create_msg(request, username):
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
    def get_msgs(request, username):
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

    @staticmethod
    def get_last_x(request, username):
        user = request.user
        interlocutor = get_object_or_404(User, username=username)
        if request.user.username == username:
            return Response({"detail": "you can't chat with yourself"}, status=status.HTTP_400_BAD_REQUEST)

        x = request.data.get("x")

        user_messages = Message.objects.filter(sender=user, receiver=interlocutor)
        interlocutor_messages = Message.objects.filter(sender=interlocutor, receiver=user)

        result_list = sorted(chain(user_messages, interlocutor_messages), key=attrgetter('created'), reverse=False)

        if x is None or x == '':
            x = 20

        if not x.isdecimal():
            x = 20

        x = int(x)
        if x > 1:
            result_list = result_list[-x:]
        list_serializer = MessageSerializer(result_list, many=True)

        return Response({'detail': list_serializer.data}, status=status.HTTP_200_OK)

    @staticmethod
    def get_new(request, username):
        user = request.user
        interlocutor = get_object_or_404(User, username=username)

        last_date = request.data.get("last_date")

        if request.user.username == username:
            return Response({"detail": "you can't chat with yourself"}, status=status.HTTP_400_BAD_REQUEST)

        user_messages = Message.objects.filter(sender=user, receiver=interlocutor, created__gt=last_date)
        interlocutor_messages = Message.objects.filter(sender=interlocutor, receiver=user, created__gt=last_date)

        result_list = sorted(chain(user_messages, interlocutor_messages), key=attrgetter('created'), reverse=False)
        list_serializer = MessageSerializer(result_list, many=True)

        return Response({'detail': list_serializer.data}, status=status.HTTP_200_OK)

from django.urls import path

from .views import ConversationView

app_name = 'chat'

urlpatterns = [
    path('<str:username>', ConversationView.as_view(), name="conversation"),
]

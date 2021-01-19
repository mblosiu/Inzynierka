from django.urls import path

from .views import ConversationView

app_name = 'chat'

urlpatterns = [
    path('<str:username>/send-msg', ConversationView.as_view({'post': 'create_msg'}), name="send-msg"),
    path('<str:username>/get-all-msgs', ConversationView.as_view({'get': 'get_msgs'}), name="conversation"),
    path('<str:username>/get-last-x-msgs', ConversationView.as_view({'get': 'get_last_x'}), name="conversation"),
    path('<str:username>/get-new-msgs', ConversationView.as_view({'get': 'get_new'}), name="conversation"),
]

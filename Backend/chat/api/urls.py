from django.urls import path

from .views import ConversationView

app_name = 'chat'

urlpatterns = [
    path('<str:username>/send-msg', ConversationView.as_view({'post': 'create_msg'}), name="send-msg"),
    path('<str:username>/get-all-msgs', ConversationView.as_view({'get': 'get_msgs'}), name="get_msgs"),
    path('<str:username>/get-last-x-msgs', ConversationView.as_view({'get': 'get_last_x'}), name="get_last_x"),
    path('<str:username>/get-new-msgs', ConversationView.as_view({'get': 'get_new'}), name="get_new"),
    path('get-all-messages-sent-by-user-pk', ConversationView.as_view({'get': 'get_all_messages_sent_by_user_pk'}),
         name="get_all_messages_sent_by_user_pk"),
    path('get-all-messages-received-by-user-pk', ConversationView.as_view({'get': 'get_all_messages_received_by_user_pk'}), name="get_all_messages_received_by_user_pk"),
]

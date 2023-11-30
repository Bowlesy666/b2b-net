"""
URL patterns for the user mailbox app:

1. `conversation_archive/<int:pk>/`:
   - URL pattern for archiving a conversation.
   - Uses an integer parameter (pk) to identify the conversation.
   - Maps to the `UserMailBoxArchiveView` view.

2. `conversation_archive_list/`:
   - URL pattern for listing archived conversations.
   - Maps to the `UserMailBoxArchiveListView` view.

3. `conversation_list/`:
   - URL pattern for listing user conversations.
   - Maps to the `UserMailBoxListView` view.

4. `conversation_create/`:
   - URL pattern for creating a new conversation.
   - Maps to the `UserMailBoxCreateMessageView` view.

5. `user_mailbox_message_detail/<int:pk>/`:
   - URL pattern for displaying details of a conversation.
   - Uses an integer parameter (pk) to identify the conversation.
   - Maps to the `UserMailBoxDetailView` view.

6. `user_mailbox_message_detail/<int:pk>/create-message/`:
   - URL pattern for creating a new message in a conversation.
   - Uses an integer parameter (pk) to identify the conversation.
   - Maps to the `CreateMessage` view.
"""
from . import views
from django.urls import path
from usermailbox.views import (
    UserMailBoxListView, UserMailBoxCreateMessageView,
    CreateMessage, UserMailBoxArchiveView,
    UserMailBoxArchiveListView
)


urlpatterns = [
    path('conversation_archive/<int:pk>/',
         views.UserMailBoxArchiveView.as_view(), name='conversation_archive'),
    path('conversation_archive_list/',
         views.UserMailBoxArchiveListView.as_view(),
         name='conversation_archive_list'),
    path('conversation_list/',
         views.UserMailBoxListView.as_view(), name='conversation_list'),
    path('conversation_create/',
         views.UserMailBoxCreateMessageView.as_view(),
         name='conversation_create'),
    path('user_mailbox_message_detail/<int:pk>/',
         views.UserMailBoxDetailView.as_view(),
         name='user_mailbox_message_detail'),
    path('user_mailbox_message_detail/<int:pk>/create-message/',
         CreateMessage.as_view(), name='create-message'),
]

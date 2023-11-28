from . import views
from django.urls import path
from .views import UserMailBoxListView, UserMailBoxCreateMessageView, CreateMessage, UserMailBoxArchiveView, UserMailBoxArchiveListView


urlpatterns = [
    path('conversation_archive/<int:pk>/', views.UserMailBoxArchiveView.as_view(), name='conversation_archive'),
    path('conversation_archive_list/', views.UserMailBoxArchiveListView.as_view(), name='conversation_archive_list'),
    path('conversation_list/', views.UserMailBoxListView.as_view(), name='conversation_list'),
    path('conversation_create/', views.UserMailBoxCreateMessageView.as_view(), name='conversation_create'),
    path('user_mailbox_message_detail/<int:pk>/', views.UserMailBoxDetailView.as_view(), name='user_mailbox_message_detail'),
    path('user_mailbox_message_detail/<int:pk>/create-message/', CreateMessage.as_view(), name='create-message'),
]

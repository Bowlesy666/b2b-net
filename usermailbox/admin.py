from django.contrib import admin
from .models import ConversationModel, MessageModel
from django_summernote.admin import SummernoteModelAdmin

@admin.register(MessageModel)
class UserMailBoxMessageAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the coversation model.
    """
    list_display = (
        'conversation',
        'message_body',
    )
    search_fields = [
        'message_body',
    ]
    list_filter = (
        'conversation',
        'message_body',
    )
    summernote_fields = ('message_body',)


@admin.register(ConversationModel)
class UserMailBoxConversationAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the coversation model.
    """
    list_display = (
        'sender_profile',
        'receiver_profile',
        'slug',
    )
    search_fields = [
        'sender_profile',
        'receiver_profile',
        'slug',
    ]
    list_filter = (
        'sender_profile',
        'receiver_profile',
        'slug',
    )

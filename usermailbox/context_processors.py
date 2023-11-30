from .models import MessageModel, ConversationModel
from django.db.models import Q


def unread_messages_count(request):
    conversation_messages_unread = {}
    if request.user.is_authenticated and hasattr(request.user, 'userprofile'):
        user_profile = request.user.userprofile
        conversations = ConversationModel.objects.filter(
            Q(sender_profile=user_profile) | Q(receiver_profile=user_profile)
        )
        total_messages_unread = 0

        for conversation in conversations:
            opposite_profile = conversation.receiver_profile if conversation.sender_profile == user_profile else conversation.sender_profile

            unread_messages_count = MessageModel.objects.filter(
                conversation=conversation,
                sender_profile=opposite_profile,
                is_read=False
            ).count()

            total_messages_unread += unread_messages_count
            conversation_messages_unread[conversation.pk] = unread_messages_count
            

    else:
        total_messages_unread = 0

    return {
        'total_messages_unread': total_messages_unread,
        "conversation_messages_unread": conversation_messages_unread,
        }

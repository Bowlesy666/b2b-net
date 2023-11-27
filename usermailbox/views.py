from django.shortcuts import render
from usermailbox import models
from django.views import generic, View
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.db.models import Q
from .models import ConversationModel, MessageModel


class UserMailBoxListView(generic.ListView):
    """
    View for listing user messages
    """
    model = ConversationModel
    template_name = 'usermailbox/conversation_list.html'
    context_object_name = 'conversation_list'

    def get_queryset(self):
        # Get the current user
        user = self.request.user

        # Filter referrals where the user is either the sender or receiver
        return ConversationModel.objects.filter(
            Q(referral_sender_id=user.userprofile) | Q(referral_receiver_id=user.userprofile),
            is_trash=False
        )

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserMailBoxCreateForm, UserMailBoxMessageForm
from django.views import generic, View
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.db.models import Q
from .models import ConversationModel, MessageModel
from userprofile.views import UserProfile


class UserMailBoxCreateMessageView(View):
    def get(self, request, *args, **kwargs):
        form = UserMailBoxCreateForm(user=request.user)
        context = {
            'form': form
        }
        return render(request, 'usermailbox/user_mailbox_create_form.html', context)

    def post(self, request, *args, **kwargs):
        form = UserMailBoxCreateForm(request.POST, user=request.user)

        if form.is_valid():
            receiver_username = form.cleaned_data['receiver_profile'].user.username
            try:
                receiver_profile = UserProfile.objects.get(user__username=receiver_username)

                if ConversationModel.objects.filter(
                    sender_profile=request.user.userprofile,
                    receiver_profile=receiver_profile
                ).exists():
                    conversation = ConversationModel.objects.filter(
                        sender_profile=request.user.userprofile,
                        receiver_profile=receiver_profile
                    ).first()
                    return redirect('user_mailbox_message_detail', pk=conversation.pk)

                conversation = ConversationModel.objects.create(
                    sender_profile=request.user.userprofile,
                    receiver_profile=receiver_profile,
                    conversation_subject=form.cleaned_data['conversation_subject']
                )
                return redirect('user_mailbox_message_detail', pk=conversation.pk)
            except:
                # Handle the case where the UserProfile for the given username doesn't exist
                return redirect('conversation_create')
        
        # If the form is not valid, re-render the form with errors
        context = {
            'form': form
        }
        return render(request, 'usermailbox/user_mailbox_create_form.html', context)

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
            Q(sender_profile=user.userprofile) | Q(receiver_profile=user.userprofile),
            is_trash=False
        )


class UserMailBoxDetailView(View):
    """
    View for displaying a blog post in detail and handling comments and likes.
    """
    def get(self, request, pk, *args, **kwargs):
        form = UserMailBoxMessageForm
        conversation = ConversationModel.objects.get(pk=pk)
        message_list = MessageModel.objects.filter(conversation__pk__contains=pk)
        context = {
        'conversation': conversation,
        'form': form,
        'message_list': message_list
        }
        return render(request, 'usermailbox/user_mailbox_message_form.html', context)


class CreateMessage(View):
  def post(self, request, pk, *args, **kwargs):
    conversation = ConversationModel.objects.get(pk=pk)
    if conversation.receiver_profile == request.user:
      receiver_profile = conversation.sender_profile
    else:
      receiver_profile = conversation.receiver_profile
      message = MessageModel(
        conversation=conversation,
        sender_profile=request.user.userprofile,
        receiver_profile=receiver_profile,
        message_body=request.POST.get('message_body'),
      )
      message.save()
      return redirect('user_mailbox_message_detail', pk=pk)

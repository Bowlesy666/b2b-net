from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic, View
from django.views.generic import UpdateView
from django.db.models import Q
from .forms import (
    UserMailBoxCreateForm,
    UserMailBoxMessageForm,
    UserMailBoxArchiveForm
)
from .models import ConversationModel, MessageModel
from userprofile.views import UserProfile


class UserMailBoxCreateMessageView(LoginRequiredMixin, View):
    """
    View for creating a new message in the user mailbox.
    """
    def get(self, request, *args, **kwargs):
        form = UserMailBoxCreateForm(user=request.user)
        context = {
            'form': form
        }
        return render(
            request, 'usermailbox/user_mailbox_create_form.html', context)

    def post(self, request, *args, **kwargs):
        form = UserMailBoxCreateForm(request.POST, user=request.user)

        if form.is_valid():
            receiver_username = form.cleaned_data[
                'receiver_profile'].user.username
            try:
                receiver_profile = UserProfile.objects.get(
                    user__username=receiver_username)

                conversation = ConversationModel.objects.filter(
                    Q(
                        sender_profile=request.user.userprofile,
                        receiver_profile=receiver_profile) |
                    Q(
                        sender_profile=receiver_profile,
                        receiver_profile=request.user.userprofile)
                ).first()

                if conversation is None:
                    conversation = ConversationModel.objects.create(
                        sender_profile=request.user.userprofile,
                        receiver_profile=receiver_profile
                    )

                return redirect(
                    'user_mailbox_message_detail', pk=conversation.pk)

            except UserProfile.DoesNotExist:
                return redirect('conversation_create')

        context = {
            'form': form
        }
        return render(
            request, 'usermailbox/user_mailbox_create_form.html', context)


class UserMailBoxListView(LoginRequiredMixin, generic.ListView):
    """
    View for listing user messages
    """
    def get(self, request, *args, **kwargs):
        conversation_list = ConversationModel.objects.filter(
            Q(sender_profile=request.user.userprofile) | Q(
                receiver_profile=request.user.userprofile
            ), is_archived=False)
        context = {
            'conversation_list': conversation_list
        }
        return render(request, 'usermailbox/conversation_list.html', context)


class UserMailBoxArchiveListView(LoginRequiredMixin, generic.ListView):
    """
    View for listing user messages
    """
    def get(self, request, *args, **kwargs):
        conversation_list = ConversationModel.objects.filter(
            Q(sender_profile=request.user.userprofile) | Q(
                receiver_profile=request.user.userprofile), is_archived=True)
        context = {
            'conversation_list': conversation_list
        }
        return render(request, 'usermailbox/archive_list.html', context)


class UserMailBoxDetailView(LoginRequiredMixin, View):
    """
    View for displaying a blog post in detail and handling comments and likes.
    """
    def get(self, request, pk, *args, **kwargs):
        form = UserMailBoxMessageForm
        conversation = ConversationModel.objects.get(pk=pk)
        message_list = MessageModel.objects.filter(
            conversation__pk__contains=pk)
        for message in message_list:
            if message.sender_profile != self.request.user.userprofile:
                message.is_read = True
                message.save(update_fields=('is_read',))

        context = {
            'conversation': conversation,
            'form': form,
            'message_list': message_list
        }
        return render(
            request, 'usermailbox/user_mailbox_message_form.html', context)


class CreateMessage(LoginRequiredMixin, View):
    """
    View for creating user messages
    """
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


class UserMailBoxArchiveView(LoginRequiredMixin, UpdateView):
    """
    View to archive user conversations
    """
    model = ConversationModel
    template_name = 'usermailbox/user_mailbox_conversation_archive.html'
    form_class = UserMailBoxArchiveForm
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
    success_url = reverse_lazy('conversation_list')

    def form_valid(self, form):
        messages.success(self.request, 'Conversation successfully moved.')
        return super().form_valid(form)

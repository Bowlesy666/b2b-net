from django import forms
from .models import ConversationModel, MessageModel
from userprofile.models import UserProfile


class UserMailBoxCreateForm(forms.ModelForm):
    """
    Form for joining a conversation
    """
    def __init__(self, *args, **kwargs):
        """
        Remove logged in user from drop down
        """
        user = kwargs.pop('user', None)
        super(UserMailBoxCreateForm, self).__init__(*args, **kwargs)

        # Exclude the logged-in user from the receiver choices
        if user:
            self.fields[
                'receiver_profile'].queryset = UserProfile.objects.exclude(
                user=user)

    class Meta:
        model = ConversationModel
        fields = [
            'receiver_profile',
        ]
        widgets = {
            'receiver_profile': forms.Select(attrs={'class': 'form-control'}),
        }


class UserMailBoxMessageForm(forms.ModelForm):
    """
    Form for creating messages
    """
    class Meta:
        model = MessageModel
        fields = [
            'message_body',
        ]
        widgets = {
            'message_body': forms.Textarea(
                attrs={'class': 'form-control text-area-height'}),
        }


class UserMailBoxArchiveForm(forms.ModelForm):
    """
    Form to confirm archive conversation
    """
    class Meta:
        model = ConversationModel
        fields = [
            'is_archived',
        ]

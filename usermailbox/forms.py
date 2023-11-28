from django import forms
from .models import ConversationModel, MessageModel
from userprofile.models import UserProfile



class UserMailBoxCreateForm(forms.ModelForm):
    """
    Form for updating the user profile information
    """
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(UserMailBoxCreateForm, self).__init__(*args, **kwargs)

        # Exclude the logged-in user from the receiver choices
        if user:
            self.fields['receiver_profile'].queryset = UserProfile.objects.exclude(
                user=user)

    class Meta:
        model = ConversationModel
        fields = [
            'receiver_profile',
            'conversation_subject',
        ]
        widgets = {
            'receiver_profile': forms.Select(attrs={'class': 'form-control'}),
            'conversation_subject': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UserMailBoxMessageForm(forms.ModelForm):
    """
    Form for updating the user profile information
    """
    class Meta:
        model = MessageModel
        fields = [
            'message_body',
        ]
        widgets = {
            'message_body': forms.TextInput(attrs={'class': 'form-control'}),
        }

from django import forms
from .models import Booking
from userprofile.models import UserProfile
from django.contrib.auth.models import User


class CreateBookingForm(forms.ModelForm):
    """
    Form for 1-2-1 Booking Creation
    """
    class Meta:
        model = Booking
        fields = [
            'receiver',
            'meeting_subject',
            'meeting_description',
            'meeting_location',
            'meeting_date',
            'meeting_time',
            'meeting_duration',
            'additional_notes',
        ]
        widgets = {
            'receiver': forms.Select(attrs={'class': 'form-control'}),
            'meeting_subject': forms.TextInput(attrs={'class': 'form-control'}),
            'meeting_description': forms.Textarea(attrs={'class': 'form-control'}),
            'meeting_location': forms.TextInput(attrs={'class': 'form-control'}),
            'meeting_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format='%Y-%m-%d'),
            'meeting_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}, format='%H:%M'),
            'meeting_duration': forms.Select(attrs={'class': 'form-control'}),
            'additional_notes': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CreateBookingForm, self).__init__(*args, **kwargs)

        # Exclude the logged-in user from the receiver choices
        if user:
            self.fields['receiver'].queryset = User.objects.exclude(id=user.id)


class UpdateBookingForm(forms.ModelForm):
    """
    Form for 1-2-1 Booking Creation
    """
    class Meta:
        model = Booking
        fields = [
            'meeting_subject',
            'meeting_description',
            'meeting_location',
            'meeting_date',
            'meeting_time',
            'meeting_duration',
            'is_accepted',
            'additional_notes',
        ]
        widgets = {
            'receiver': forms.Select(attrs={'class': 'form-control'}),
            'meeting_subject': forms.TextInput(attrs={'class': 'form-control'}),
            'meeting_description': forms.Textarea(attrs={'class': 'form-control'}),
            'meeting_location': forms.TextInput(attrs={'class': 'form-control'}),
            'meeting_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format='%Y-%m-%d'),
            'meeting_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}, format='%H:%M'),
            'meeting_duration': forms.Select(attrs={'class': 'form-control'}),
            'additional_notes': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CancelBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['is_cancelled',]

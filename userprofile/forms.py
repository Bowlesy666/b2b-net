from django import forms
from .models import UserProfile
from allauth.account.forms import SignupForm
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
    """
    Form for updating the user profile information
    """
    class Meta:
        model = UserProfile
        fields = [
            'user_profile_img',
            'user_contact_number',
            'display_user_email',
            'user_about',
            'company_name',
            'business_sector',
            'company_website',
            'company_contact_email',
            'company_contact_number',
            'alternative_company_contact_number',
            'company_bio',
            'company_services_post',
            'company_hero_picture',
        ]
        widgets = {
            'company_bio': forms.Textarea(attrs={'class': 'form-control'}),
            'business_sector': forms.Select(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_website': forms.TextInput(attrs={'class': 'form-control'}),
            'company_contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'alternative_company_contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'company_contact_email': forms.TextInput(attrs={'class': 'form-control'}),
            'company_services_post': forms.Textarea(attrs={'class': 'form-control'}),
            'company_hero_picture': forms.FileInput(attrs={'class': 'form-control'}),
            'user_contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'user_about': forms.Textarea(attrs={'class': 'form-control'}),
            'user_profile_img': forms.FileInput(attrs={'class': 'form-control'}),
        }


class UserForm(forms.ModelForm):
    """
    Form for updating basic user information
    """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
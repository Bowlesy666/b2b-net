from django import forms
from .models import ReferralsModel
from userprofile.models import UserProfile


class CreateReferralsForm(forms.ModelForm):
    """
    Form for Referrals Creation
    """

    def __init__(self, *args, **kwargs):
        """
        Excludes logged in user from drop down choices
        """
        user = kwargs.pop('user', None)
        super(CreateReferralsForm, self).__init__(*args, **kwargs)

        if user:
            self.fields[
                'referral_receiver_id'
                ].queryset = UserProfile.objects.exclude(
                user=user)

    class Meta:
        model = ReferralsModel
        fields = [
            'referral_receiver_id',
            'referral_subject',
            'referral_description',
            'introduced_person_name',
            'introduced_person_company',
            'introduced_person_email',
            'introduced_person_phonenumber',
            'introduced_person_alternative_phonenumber',
            'proposed_amount',
            'percentage',
            'expected_completion_date',
        ]
        widgets = {
            'referral_receiver_id': forms.Select(
                attrs={'class': 'form-control'}),
            'referral_subject': forms.TextInput(
                attrs={'class': 'form-control'}),
            'referral_description': forms.Textarea(
                attrs={'class': 'form-control'}),
            'introduced_person_name': forms.TextInput(
                attrs={'class': 'form-control'}),
            'introduced_person_company': forms.TextInput(
                attrs={'class': 'form-control'}),
            'introduced_person_email': forms.TextInput(
                attrs={'class': 'form-control'}),
            'introduced_person_phonenumber': forms.TextInput(
                attrs={'class': 'form-control'}),
            'introduced_person_alternative_phonenumber': forms.TextInput(
                attrs={'class': 'form-control'}),
            'proposed_amount': forms.NumberInput(),
            'percentage': forms.NumberInput(),
            'expected_completion_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'},
                format='%Y-%m-%d'),
        }


class ReferralsUpdateForm(forms.ModelForm):
    """
    Form for referrals updating
    """
    class Meta:
        model = ReferralsModel
        fields = [
            'referral_subject',
            'referral_description',
            'introduced_person_name',
            'introduced_person_company',
            'introduced_person_email',
            'introduced_person_phonenumber',
            'introduced_person_alternative_phonenumber',
            'proposed_amount',
            'percentage',
            'expected_completion_date',
        ]
        widgets = {
            'referral_subject': forms.TextInput(
                attrs={'class': 'form-control'}),
            'referral_description': forms.Textarea(
                attrs={'class': 'form-control'}),
            'introduced_person_name': forms.TextInput(
                attrs={'class': 'form-control'}),
            'introduced_person_company': forms.TextInput(
                attrs={'class': 'form-control'}),
            'introduced_person_email': forms.TextInput(
                attrs={'class': 'form-control'}),
            'introduced_person_phonenumber': forms.TextInput(
                attrs={'class': 'form-control'}),
            'introduced_person_alternative_phonenumber': forms.TextInput(
                attrs={'class': 'form-control'}),
            'proposed_amount': forms.NumberInput(),
            'percentage': forms.NumberInput(),
            'expected_completion_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'},
                format='%Y-%m-%d'),
        }


class ReferralsArchiveForm(forms.ModelForm):
    """
    Form for referrals archiving
    """
    class Meta:
        model = ReferralsModel
        fields = ['is_archived']


class ReferralsConfirmAgreementForm(forms.ModelForm):
    """
    Form for referrals confirmation
    """
    class Meta:
        model = ReferralsModel
        fields = ['is_agreed']


class ReferralsAgreementCompletedForm(forms.ModelForm):
    """
    Form for referrals Agreement by both parties
    """
    class Meta:
        model = ReferralsModel
        fields = ['is_completed']


class ReferralsCancelForm(forms.ModelForm):
    """
    Form for referrals cancellation
    """
    class Meta:
        model = ReferralsModel
        fields = ['is_cancelled', 'cancellation_reason']
        widgets = {'cancellation_reason': forms.Textarea(
            attrs={'class': 'form-control'})}

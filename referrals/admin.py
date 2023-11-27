from django.contrib import admin
from .models import ReferralsModel
from django_summernote.admin import SummernoteModelAdmin

@admin.register(ReferralsModel)
class ReferralsAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the Post model.
    """
    list_display = (
        'referral_sender_id',
        'referral_receiver_id',
        'referral_subject',
        'introduced_person_company',
        'estimated_commsion',
        'is_agreed',
        'is_cancelled',
        'is_completed',
        'is_archived',
    )
    search_fields = [
        'referral_sender_id',
        'referral_receiver_id',
        'referral_subject',
        'introduced_person_company',
        'estimated_commsion',
    ]
    list_filter = (
        'referral_sender_id',
        'referral_receiver_id',
        'referral_subject',
        'introduced_person_company',
        'estimated_commsion',
        'is_agreed',
        'is_cancelled',
        'is_completed',
        'is_archived',
    )
    summernote_fields = ('referral_description', 'cancellation_reason',)

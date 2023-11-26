from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the Post model.
    """
    list_display = ('sender', 'receiver', 'meeting_subject', 'is_accepted', 'is_cancelled', 'is_archived')
    search_fields = ['sender', 'receiver', 'meeting_subject', 'is_accepted', 'is_cancelled', 'is_archived']
    list_filter = ('sender', 'receiver', 'meeting_subject', 'is_cancelled', 'is_archived')
    summernote_fields = ('meeting_description', 'additional_notes',)

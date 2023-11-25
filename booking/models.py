from django.db import models
from userprofile.models import UserProfile
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.crypto import get_random_string


MEETING_DURATION_CHOICES = (
    ('30_mins', '30 mins'),
    ('45_mins', '46 mins'),
    ('60_mins', '1 hour'),
    ('75_mins', '1 hour 15 mins'),
    ('90_mins', '1 hour 30 mins'),
    ('105_mins', '1 hour 45 mins'),
    ('120_mins', '2 hours MAX'),
)


class Booking(models.Model):
    sender = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='booking_sender')
    receiver = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='booking_receiver')
    meeting_subject = models.CharField(max_length=100, null=False)
    meeting_description = models.TextField()
    meeting_location = models.CharField(max_length=100, null=False)
    meeting_date = models.DateField(null=False, validators=[RegexValidator(
        r'\d{4}-\d{2}-\d{2}', message='Enter a valid date format (DD-MM-YYYY)')])
    meeting_time = models.TimeField(null=False, validators=[RegexValidator(
        r'\d{2}:\d{2}', message='Enter a valid time format (HH:MM)')])
    meeting_duration = models.CharField(
        max_length=50, choices=MEETING_DURATION_CHOICES, default='30_mins')
    is_accepted = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    additional_notes = models.TextField()
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

    class Meta:
        """
        Order bookings by meeting date in descending order.
        """
        ordering = ["-meeting_date"]

    def __str__(self):
        return f'Meeting for: {self.sender.user.username} & {self.receiver.user.username} - {self.meeting_subject}'

    def save(self, *args, **kwargs):
        """
        Override the save method to auto-generate the slug.
        """
        print(
            f"Saving Booking with date: {self.meeting_date} and time: {self.meeting_time}")

        if not self.slug:
            slug_save(self)  # call slug_save, listed below
            super(Booking, self).save(*args, **kwargs)
        super().save(*args, **kwargs)


def slug_save(obj):
    """
    Generates a 5 character slug and checks to see if it has been used
    """
    if not obj.slug:  # if there isn't a slug
        obj.slug = get_random_string(5)  # create one
        slug_is_wrong = True
        while slug_is_wrong:  # keep checking until we have a valid slug
            slug_is_wrong = False
            other_objs_with_slug = type(obj).objects.filter(slug=obj.slug)
            if len(other_objs_with_slug) > 0:
                # if any other objects have current slug
                slug_is_wrong = True
            if slug_is_wrong:
                # create another slug and check it again
                obj.slug = get_random_string(5)

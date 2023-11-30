from django.db import models
from userprofile.models import UserProfile
from phonenumber_field.modelfields import PhoneNumberField
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
from django.core.validators import RegexValidator
from django.utils.crypto import get_random_string


class ReferralsModel(models.Model):
    """
    Model representing a referral instance.
    """
    referral_sender_id = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE,
        related_name='sent_referrals')
    referral_receiver_id = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE,
        related_name='received_referrals')
    referral_subject = models.CharField(max_length=100, null=False)
    referral_description = models.TextField()
    introduced_person_name = models.CharField(max_length=100, null=False)
    introduced_person_company = models.CharField(max_length=100)
    introduced_person_email = models.EmailField(
        max_length=100, blank=True, unique=True)
    introduced_person_phonenumber = PhoneNumberField(
        unique=True, region='GB', null=False)
    introduced_person_alternative_phonenumber = PhoneNumberField(
        unique=True, region='GB')
    proposed_amount = models.DecimalField(
        max_digits=10, decimal_places=2)
    percentage = models.DecimalField(
        max_digits=4, decimal_places=2, default=5.00)
    expected_completion_date = models.DateField(
        null=True,
        validators=[RegexValidator(r'\d{4}-\d{2}-\d{2}',
                    message='Enter a valid date format (DD-MM-YYYY)')])
    estimated_commsion = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    is_percentage_editable = models.BooleanField(default=True)
    is_agreed = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)
    cancellation_reason = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    slug = models.SlugField(
        max_length=200, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.referral_sender_id.user.username}{self.proposed_amount}"

    def calculate_commission(self):
        """
        Calculate commission based on the proposed amount and percentage.
        """
        return (self.proposed_amount * self.percentage) / 100

    def clean(self):
        """
        Override the clean method to ensure data consistency.
        """
        super().clean()

        if not self.is_percentage_editable:
            self.percentage = 5.00
        self.estimated_commsion = self.calculate_commission()

    def save(self, *args, **kwargs):
        """
        Override the save method to auto-generate the slug.
        """
        print(
            f"Saving Referral: {self.referral_subject}")

        if not self.slug:
            slug_save(self)  # call slug_save, listed below
            super(ReferralsModel, self).save(*args, **kwargs)
        self.clean()
        super().save(*args, **kwargs)


def slug_save(obj):
    """
    Generates a 5 character slug and checks to see if it has been used
    """
    if not obj.slug:
        obj.slug = get_random_string(5)
        slug_is_wrong = True
        while slug_is_wrong:
            slug_is_wrong = False
            other_objs_with_slug = type(obj).objects.filter(slug=obj.slug)
            if len(other_objs_with_slug) > 0:
                slug_is_wrong = True
            if slug_is_wrong:
                obj.slug = get_random_string(5)

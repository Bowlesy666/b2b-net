from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


BUSINESS_SECTOR_CHOICES = (
    ('other', 'Other...'),
    ('accounting', 'Accounting'),
    ('analytics', 'Analytics & Market Research'),
    ('construction', 'Construction'),
    ('education', 'Education'),
    ('energy', 'Oil, Gas & Electricity'),
    ('energy_renewable', 'Renewable Energy'),
    ('engineering', 'Engineering'),
    ('estate_agent', 'Estate Agency'),
    ('entrepreneur', 'Entrepreneur'),
    ('finance', 'Finance'),
    ('food', 'Food Production'),
    ('health_care', 'Health Care'),
    ('hospitality', 'Hospitality'),
    ('insurance', 'Insurance'),
    ('law', 'Law'),
    ('logistics', 'Transport & Logistics'),
    ('management', 'Management'),
    ('manufacturing', 'Manufacturing'),
    ('marketing', 'Marketing'),
    ('management_consulting', 'Management Consulting'),
    ('recruitment', 'Recruitment Agency'),
    ('retail', 'Retail'),
    ('technology', 'Technology'),
    ('telecomms', 'IT & Telecommunication'),
    ('warehouse', 'Warehousing & Operations'),
)


class UserProfile(models.Model):
    """
    Model representing user profiles for businesses.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(
        max_length=200, unique=True, null=True, blank=True)
    business_sector = models.CharField(
        max_length=50, choices=BUSINESS_SECTOR_CHOICES, default='other',
        help_text="Select the business sector for the user.", blank=False
    )
    company_name = models.CharField(
        max_length=100, help_text="Enter your company name.", blank=False,
        default='Ask me what my company name is...')
    company_website = models.URLField(
        max_length=200, null=True,
        help_text="Enter your company website URL.", blank=True)
    company_contact_number = PhoneNumberField(
        unique=False, region='GB', null=True,
        help_text="Primary contact number for the company.", blank=True
    )
    alternative_company_contact_number = PhoneNumberField(
        unique=False, region='GB', null=True,
        help_text="Alternative contact number for the company.", blank=True
    )
    company_contact_email = models.EmailField(
        unique=False, null=True,
        help_text="Enter your company contact email.", blank=True)
    company_bio = models.TextField(
        null=True, help_text="Provide a brief bio about your company.",
        blank=True)
    company_services_post = models.TextField(
        null=True, help_text="Post about your company services.", blank=True)
    company_hero_picture = CloudinaryField(
        'image', default='placeholder',
        help_text="Upload a hero picture for your company.", blank=False)
    user_contact_number = PhoneNumberField(
        unique=True, region='GB', null=True,
        help_text="Your personal contact number.", blank=False
    )
    display_user_email = models.BooleanField(
        default=True, help_text="Display user email publicly.")
    user_about = models.TextField(
        help_text="Tell us about yourself.", blank=False,
        default='Come say hi to me...')
    user_profile_img = CloudinaryField(
        'image', default='placeholder',
        help_text="Upload your profile picture.")

    def save(self, *args, **kwargs):
        """
        Override the save method to auto-generate the slug.
        """
        if not self.slug:
            self.slug = slugify(self.company_name + '-' + str(self.pk))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username


class Review(models.Model):
    """
    Model representing reviews for user profiles.
    """
    review_from = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='reviewed_from',
        help_text="User profile giving the review."
    )
    profile_reviewed = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='profile_reviewed',
        help_text="User profile being reviewed."
    )
    stars = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating given in stars (1 to 5)."
    )
    comment = models.TextField()
    date_created = models.DateField(
        help_text="Date when the review was created."
    )
    time_created = models.TimeField(
        help_text="Time when the review was created."
    )

    objects = models.Manager()

    def save(self, *args, **kwargs):
        self.stars = self.get_average_stars_for_user(self.profile_reviewed)
        super().save(*args, **kwargs)

    @staticmethod
    def get_average_stars_for_user(user):
        """
        Get the average stars for a given user.
        """
        return Review.objects.filter(profile_reviewed=user).aggregate(
            avg_stars=models.Avg('stars')
        )['avg_stars'] or 0

    def __str__(self):
        return f"Stars Awarded - {self.stars} stars"

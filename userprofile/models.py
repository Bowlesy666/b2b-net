from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from cloudinary.models import CloudinaryField


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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    business_sector = models.CharField(
        max_length=50, choices=BUSINESS_SECTOR_CHOICES, default='other')
    company_name = models.CharField(max_length=100)
    comapny_website = models.URLField(max_length=200)
    company_contact_number = PhoneNumberField(
        unique=True, region='GB', null=False)
    alternative_company_contact_number = PhoneNumberField(
        unique=True, region='GB')
    company_contact_email = models.EmailField(unique=True)
    company_bio = models.TextField()
    company_services_post = models.TextField()
    company_hero_picture = CloudinaryField('image', default='placeholder')
    user_contact_number = PhoneNumberField(
        unique=True, region='GB', null=False)
    display_user_email = models.BooleanField(default=True)
    user_about = models.TextField()
    user_profile_img = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return f'{ self.user.username }: { self.company_name }'


class Review(models.Model):
    review_from = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviewed_from')
    profile_reviewed = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='profile_reviewed')
    stars = models.IntegerField()
    comment = models.TextField()
    date_created = models.DateField()
    time_created = models.TimeField()

    def save(self):
        user = self.reviewed
        stars = Review.objects.filter(reviewed=user).aggregate(sum(stars))

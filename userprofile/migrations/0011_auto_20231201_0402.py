# Generated by Django 3.2.23 on 2023-12-01 04:02

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0010_alter_userprofile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='alternative_company_contact_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Alternative contact number for the company.', max_length=128, null=True, region='GB', unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='company_bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='company_contact_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='company_contact_number',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Primary contact number for the company.', max_length=128, region='GB'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='company_services_post',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='company_website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_contact_number',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Your personal contact number.', max_length=128, region='GB', unique=True),
        ),
    ]
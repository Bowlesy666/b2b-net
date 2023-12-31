# Generated by Django 3.2.23 on 2023-11-20 03:32

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='alternative_company_contact_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region='GB', unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='comapny_website',
            field=models.URLField(null=True),
        ),
    ]

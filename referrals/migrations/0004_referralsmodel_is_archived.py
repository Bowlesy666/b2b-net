# Generated by Django 3.2.23 on 2023-11-26 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referrals', '0003_referralsmodel_estimated_commsion'),
    ]

    operations = [
        migrations.AddField(
            model_name='referralsmodel',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
    ]

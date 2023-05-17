# Generated by Django 4.1.3 on 2022-11-17 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfileApp', '0004_remove_profile_full_name_remove_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='0_DynamicImages/profile-picturs'),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-18 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfileApp', '0025_rename_employe_user_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'unique': 'The email must be unique!'}, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='0_DynamicImages/profile-picturs'),
        ),
    ]

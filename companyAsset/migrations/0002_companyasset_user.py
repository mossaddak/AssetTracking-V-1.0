# Generated by Django 4.2.1 on 2023-05-17 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companyAsset', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyasset',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CompanyAssetUserRelatedname', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-19 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0011_assetreturn_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetreturn',
            name='asset',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
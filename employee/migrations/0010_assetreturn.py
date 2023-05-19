# Generated by Django 4.2.1 on 2023-05-19 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0009_alter_employeev_back_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetReturn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=250, null=True)),
                ('condition', models.CharField(blank=True, max_length=250, null=True)),
                ('is_return', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]

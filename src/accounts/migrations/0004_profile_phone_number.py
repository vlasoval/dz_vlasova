# Generated by Django 4.1.2 on 2022-11-27 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_birth_date_profile_birthday_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]

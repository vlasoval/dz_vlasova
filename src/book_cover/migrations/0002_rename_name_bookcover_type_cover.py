# Generated by Django 4.1.2 on 2022-10-09 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_cover', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookcover',
            old_name='name',
            new_name='type_cover',
        ),
    ]

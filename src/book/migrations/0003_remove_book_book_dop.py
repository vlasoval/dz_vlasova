# Generated by Django 4.1.2 on 2022-10-12 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_book_dop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_dop',
        ),
    ]

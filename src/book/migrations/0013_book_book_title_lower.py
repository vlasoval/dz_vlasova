# Generated by Django 4.1.2 on 2022-12-12 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0012_bookcomments'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_title_lower',
            field=models.CharField(blank=True, editable=False, max_length=40, null=True, verbose_name='Название книги'),
        ),
    ]

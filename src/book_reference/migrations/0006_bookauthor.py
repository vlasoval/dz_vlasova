# Generated by Django 4.1.2 on 2022-10-10 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_reference', '0005_bookseries'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_author', models.CharField(max_length=40, verbose_name='Автор')),
            ],
        ),
    ]
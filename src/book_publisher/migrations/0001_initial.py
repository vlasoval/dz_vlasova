# Generated by Django 4.1.2 on 2022-10-09 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookPublisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_publisher', models.CharField(max_length=40, verbose_name='Издательство')),
            ],
        ),
    ]
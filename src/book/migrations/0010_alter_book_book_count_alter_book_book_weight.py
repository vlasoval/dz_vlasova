# Generated by Django 4.1.2 on 2022-10-23 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_alter_book_book_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_count',
            field=models.PositiveIntegerField(verbose_name='Количество книг в наличии'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_weight',
            field=models.PositiveIntegerField(verbose_name='Вес (гр)'),
        ),
    ]
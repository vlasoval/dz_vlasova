# Generated by Django 4.1.2 on 2022-10-12 17:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_book_book_active_book_book_age_book_book_count_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_active',
        ),
        migrations.AlterField(
            model_name='book',
            name='book_count',
            field=models.IntegerField(verbose_name='Количество книг в наличии'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата внесения в каталог'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_page',
            field=models.IntegerField(verbose_name='Страниц'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_rating',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)], verbose_name='Рейтинг (0 - 10)'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_weight',
            field=models.IntegerField(verbose_name='Вес (гр)'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_year',
            field=models.IntegerField(verbose_name='Год издания'),
        ),
    ]

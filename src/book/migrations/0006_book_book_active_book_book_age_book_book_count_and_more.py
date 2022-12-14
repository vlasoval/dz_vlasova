# Generated by Django 4.1.2 on 2022-10-12 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_alter_book_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_active',
            field=models.CharField(default=1, max_length=5, verbose_name='Активный (доступен для заказа, Да/Нет)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='book_age',
            field=models.CharField(default=1, max_length=5, verbose_name='Возрастные ограничения'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='book_count',
            field=models.CharField(default=1, max_length=5, verbose_name='Количество книг в наличии'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='book_cover',
            field=models.CharField(default=1, max_length=30, verbose_name='Переплет'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='book_date',
            field=models.DateField(auto_now=True, verbose_name='Дата внесения в каталог'),
        ),
        migrations.AddField(
            model_name='book',
            name='book_date_change',
            field=models.DateField(auto_now=True, verbose_name='Дата последнего изменения карточки'),
        ),
        migrations.AddField(
            model_name='book',
            name='book_format',
            field=models.CharField(default=1, max_length=40, verbose_name='Формат'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='book_isbn',
            field=models.CharField(default=1, max_length=30, verbose_name='ISBN'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='book_page',
            field=models.CharField(default=1, max_length=10, verbose_name='Страниц'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='book_rating',
            field=models.CharField(default=1, max_length=5, verbose_name='Рейтинг (0 - 10)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='book_weight',
            field=models.CharField(default=1, max_length=10, verbose_name='Вес (гр)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='book_year',
            field=models.CharField(default=1, max_length=10, verbose_name='Год издания'),
            preserve_default=False,
        ),
    ]

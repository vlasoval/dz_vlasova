# Generated by Django 4.1.2 on 2022-10-09 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_publisher', '0001_initial'),
        ('book_genre', '0001_initial'),
        ('book_year', '0002_alter_bookyear_book_year'),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_genre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='book_genre.bookgenre', verbose_name='Жанр'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='book_publisher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='book_publisher.bookpublisher', verbose_name='Издательство'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='book_year',
            field=models.ForeignKey(default=1.0, on_delete=django.db.models.deletion.PROTECT, to='book_year.bookyear', verbose_name='Год'),
            preserve_default=False,
        ),
    ]

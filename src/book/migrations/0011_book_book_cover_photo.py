# Generated by Django 4.1.2 on 2022-10-31 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_alter_book_book_count_alter_book_book_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_cover_photo',
            field=models.ImageField(default='1', upload_to='upload', verbose_name='Фото обложки'),
            preserve_default=False,
        ),
    ]
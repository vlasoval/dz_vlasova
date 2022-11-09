# Generated by Django 4.1.2 on 2022-10-23 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_book_book_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_active',
            field=models.CharField(choices=[('Yes', 'Да'), ('No', 'Нет')], default='Да', max_length=10, verbose_name='Активный (доступен для заказа)'),
        ),
    ]
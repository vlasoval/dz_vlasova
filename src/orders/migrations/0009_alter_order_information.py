# Generated by Django 4.1.2 on 2022-12-10 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_alter_order_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='information',
            field=models.TextField(blank=True, null=True, verbose_name='Добавить комментарий к заказу:'),
        ),
    ]

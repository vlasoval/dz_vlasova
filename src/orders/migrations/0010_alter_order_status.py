# Generated by Django 4.1.2 on 2022-12-12 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_alter_order_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Заказ принят', 'Заказ принят'), ('Заказ собран', 'Заказ собран'), ('Заказ отправлен', 'Заказ отправлен'), ('Заказ доставлен', 'Заказ доставлен')], default='Заказ принят', max_length=200, verbose_name='Статус'),
        ),
    ]

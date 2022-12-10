# Generated by Django 4.1.2 on 2022-12-09 17:44

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0011_book_book_cover_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('rating', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='b_comments', to='book.book')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='b_comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'BookCommentV2',
            },
        ),
    ]

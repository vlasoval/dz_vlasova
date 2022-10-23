from pyexpat import model
from random import choices
from re import T
from django import forms
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Book(models.Model):
    book_title=models.CharField(
        max_length=40,
        verbose_name='Название книги'
    )
    book_genre=models.ManyToManyField(
        'book_reference.BookGenre',
        verbose_name='Жанр',
    )
    book_publisher=models.ForeignKey(
        'book_reference.BookPublisher',
        verbose_name='Издательство',
        on_delete=models.PROTECT,
    )
    book_series=models.ForeignKey(
        'book_reference.BookSeries',
        verbose_name='Серия',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )    
    book_author=models.ManyToManyField(
        'book_reference.BookAuthor',
        verbose_name='Автор',
    )
    book_price=models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name='Цена (BYN)'
    )
    book_year=models. IntegerField(
        verbose_name='Год издания'
    )
    book_page=models.IntegerField(
        verbose_name='Страниц'
    )
    book_cover=models.CharField(
        max_length=30,
        verbose_name='Переплет'
    )
    book_format=models.CharField(
        max_length=40,
        verbose_name='Формат'
    )
    book_isbn=models.CharField(
        max_length=30,
        verbose_name='ISBN'
    )
    book_weight=models.PositiveIntegerField(
        verbose_name='Вес (гр)'
    )
    book_age=models.CharField(
        max_length=5,
        verbose_name='Возрастные ограничения'
    )
    book_count=models.PositiveIntegerField(
        verbose_name='Количество книг в наличии'
    )
    MY_CHOICES=[
        ('Yes', 'Да'),
        ('No', 'Нет'),
    ]   
    book_active=models.CharField (
        choices=MY_CHOICES,
        default='Да',
        max_length=10, 
        verbose_name='Активный (доступен для заказа)'
    )      
    book_rating=models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        verbose_name='Рейтинг (0 - 10)'
    )
    book_date=models.DateField(
        auto_now_add=True,
        verbose_name='Дата внесения в каталог'
    )    
    book_date_change=models.DateField(
        auto_now=True,
        verbose_name='Дата последнего изменения карточки'
    )        
    def __str__(self):
        return self.book_title
from distutils.command.upload import upload
from pyexpat import model
from random import choices
from re import T
from django import forms
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.db.models import Avg


User = get_user_model()
class Book(models.Model):
    book_title=models.CharField(
        max_length=40,
        verbose_name='Название книги'
        
    )
    book_cover_photo=models.ImageField(
        verbose_name='Фото обложки',
        upload_to='upload'
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
    @property
    def average_rating(self):
        return self.b_comments.all().aggregate(Avg('rating'))['rating__avg']   


class BookComments(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='b_comments')
    customer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='b_comments')
    comment = models.TextField()
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    created_date = models.DateField(auto_now=False, auto_now_add=True)
    updated_date = models.DateField(auto_now=True, auto_now_add=False)
    class Meta:
        db_table = 'BookCommentV2'
    def __str__(self):
        return str(self.pk)      


from django.db import models

# Create your models here.
class BookGenre(models.Model):
    book_genre= models.CharField(
        max_length=40,
        verbose_name='Жанр'
        )
    description=models.TextField(
        verbose_name='Описание жанра'
    )
    def __str__(self):
        return self.book_genre

    def get_absolute_url(self):
        return f'/genre_show/{self.pk}'


class BookPublisher(models.Model):
    book_publisher= models.CharField(
        max_length=40,
        verbose_name='Издательство'
        )
    def __str__(self):
        return self.book_publisher

class BookSeries(models.Model):
    book_series= models.CharField(
        max_length=40,
        verbose_name='Серия'
        )
    def __str__(self):
        return self.book_series

class BookAuthor(models.Model):
    book_author= models.CharField(
        max_length=40,
        verbose_name='Автор'
        )
    def __str__(self):
        return self.book_author



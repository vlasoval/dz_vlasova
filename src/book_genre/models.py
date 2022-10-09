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
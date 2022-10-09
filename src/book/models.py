from django.db import models

# Create your models here.
class Book(models.Model):
    book_title=models.CharField(
        max_length=40,
        verbose_name='Название книги'
    )
    type_cover=models.ForeignKey(
        'book_cover.BookCover',
        verbose_name='Тип обложки',
        on_delete=models.PROTECT,
    )
    book_genre=models.ForeignKey(
        'book_genre.BookGenre',
        verbose_name='Жанр',
        on_delete=models.PROTECT,
    )
    book_publisher=models.ForeignKey(
        'book_publisher.BookPublisher',
        verbose_name='Издательство',
        on_delete=models.PROTECT,
    )
    book_year=models.ForeignKey(
        'book_year.BookYear',
        verbose_name='Год',
        on_delete=models.PROTECT,
    )    
    def __str__(self):
        return self.book_title
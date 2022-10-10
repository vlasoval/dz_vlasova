from django.db import models

# Create your models here.
class Book(models.Model):
    book_title=models.CharField(
        max_length=40,
        verbose_name='Название книги'
    )
    # type_cover=models.ForeignKey(
    #     'book_cover.BookCover',
    #     verbose_name='Тип обложки',
    #     on_delete=models.PROTECT,
    # )
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
    def __str__(self):
        return self.book_title

    book_author=models.ManyToManyField(
        'book_reference.BookAuthor',
        verbose_name='Автор',
    )
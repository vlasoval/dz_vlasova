from django.db import models

# Create your models here.
class BookPublisher(models.Model):
    book_publisher= models.CharField(
        max_length=40,
        verbose_name='Издательство'
        )
    def __str__(self):
        return self.book_publisher
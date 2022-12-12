from django.db import models
from django.urls import reverse_lazy

# Create your models here.
class BookGenre(models.Model):
    name= models.CharField(
        max_length=40,
        verbose_name='Жанр'
        )
    description=models.TextField(
        verbose_name='Описание жанра',
        blank=True,
        null=True
    )
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('book_reference:genre-detail', kwargs={'pk':self.pk})


class BookPublisher(models.Model):
    name= models.CharField(
        max_length=40,
        verbose_name='Издательство'
        )
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse_lazy('book_reference:publisher-detail', kwargs={'pk':self.pk})

class BookSeries(models.Model):
    name= models.CharField(
        max_length=40,
        verbose_name='Серия'
        )
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse_lazy('book_reference:series-detail', kwargs={'pk':self.pk})

class BookAuthor(models.Model):
    name= models.CharField(
        max_length=40,
        verbose_name='Автор'
        )

    name_lower=models.CharField(
        max_length=40,
        verbose_name='Автор',
        editable=False,
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        self.name_lower=self.name.lower() if self.name else None
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('book_reference:author-detail', kwargs={'pk':self.pk})



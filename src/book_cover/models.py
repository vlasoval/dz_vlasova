from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class BookCover(models.Model):
    type_cover= models.CharField(
        max_length=40,
        verbose_name='Тип обложки'
        )

    def __str__(self):
        return self.type_cover
from dataclasses import fields
from django import forms
from django import forms
from django.forms import ModelForm
from . import models

class GenreForm(ModelForm):
    class Meta:
        model = models.BookGenre
        fields = [
            'book_genre',
            'description'
            ] 

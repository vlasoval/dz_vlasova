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

class AuthorForm(ModelForm):
    class Meta:
        model = models.BookAuthor
        fields = [
            'book_author',
            ]             

class PublisherForm(ModelForm):
    class Meta:
        model = models.BookPublisher
        fields = [
            'book_publisher',
            ]   

class SeriesForm(ModelForm):
    class Meta:
        model = models.BookSeries
        fields = [
            'book_series',
            ]              
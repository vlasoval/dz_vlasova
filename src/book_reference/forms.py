from dataclasses import fields
from django import forms
from django import forms
from django.forms import ModelForm
from . import models

class GenreForm(ModelForm):
    class Meta:
        model = models.BookGenre
        fields = [
            'name',
            'description'
            ] 

class AuthorForm(ModelForm):
    class Meta:
        model = models.BookAuthor
        fields = [
            'name',
            ]             

class PublisherForm(ModelForm):
    class Meta:
        model = models.BookPublisher
        fields = [
            'name',
            ]   

class SeriesForm(ModelForm):
    class Meta:
        model = models.BookSeries
        fields = [
            'name',
            ]              
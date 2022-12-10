from django import forms
from .models import BookComments, Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'book_title',
            'book_cover_photo',
            'book_genre',
            'book_publisher',
            'book_series',
            'book_author',
            'book_price',
            'book_year',
            'book_page',
            'book_cover',
            'book_format',
            'book_isbn',
            'book_weight',
            'book_age',
            'book_count',
            'book_active',
            ]

class BookCommentsForm(forms.ModelForm):
    class Meta:
        model = BookComments
        fields = [
            'rating',
            'comment']

class UploadFileForm(forms.Form):
    file = forms.FileField()

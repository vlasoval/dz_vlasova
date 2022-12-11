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
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.book_pk = kwargs.pop('book_pk')
        super(BookCommentsForm, self).__init__(*args, **kwargs)

    class Meta:
        model = BookComments
        fields = [
            'rating',
            'comment']

    def clean(self):
        if BookComments.objects.filter(customer=self.user, book__pk=self.book_pk).count() > 0:
            raise forms.ValidationError("Пользователь уже имеет комментарий")

        return super().clean()

class UploadFileForm(forms.Form):
    file = forms.FileField()

class BookCommentsFormUpdate(forms.ModelForm):
    class Meta:
        model = BookComments
        fields = [
            'rating',
            'comment']
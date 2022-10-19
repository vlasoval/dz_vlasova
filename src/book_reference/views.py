from django.shortcuts import HttpResponse
from django.urls import reverse
from urllib import response
from django.shortcuts import render
from django.views import generic
from . import models, forms
import book_reference

class CreateGenre(generic.CreateView):
    model = models.BookGenre
    form_class = forms.GenreForm
    template_name = 'book_reference/create_genre.html'

class UpdateGenre(generic.UpdateView):
    model = models.BookGenre
    form_class = forms.GenreForm
    template_name = 'book_reference/update_genre.html'

class ShowGenre(generic.DetailView):
    model = models.BookGenre
    template_name = 'book_reference/detail_genre.html'

class ShowGenres(generic.ListView):
    model = models.BookGenre
    template_name = 'book_reference/list_genres.html'

class DeleteGenre(generic.DeleteView):
    model = models.BookGenre
    template_name = 'book_reference/delete_genre.html'
    success_url="/genres_show"


class CreateAuthor(generic.CreateView):
    model = models.BookAuthor
    form_class = forms.AuthorForm
    template_name = 'book_reference/create_author.html'

class UpdateAuthor(generic.UpdateView):
    model = models.BookAuthor
    form_class = forms.AuthorForm
    template_name = 'book_reference/update_author.html'

class ShowAuthor(generic.DetailView):
    model = models.BookAuthor
    template_name = 'book_reference/detail_author.html'

class ShowAuthors(generic.ListView):
    model = models.BookAuthor
    template_name = 'book_reference/list_authors.html'

class DeleteAuthor(generic.DeleteView):
    model = models.BookAuthor
    template_name = 'book_reference/delete_author.html'
    success_url="/authors_show"
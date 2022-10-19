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


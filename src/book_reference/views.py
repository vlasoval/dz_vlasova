from django.shortcuts import HttpResponse
from django.urls import reverse, reverse_lazy
from urllib import response
from django.shortcuts import render
from django.views import generic
from . import models, forms
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


class CreateGenre(PermissionRequiredMixin, LoginRequiredMixin,generic.CreateView):
    model = models.BookGenre
    form_class = forms.GenreForm
    permission_required = ("book_reference.add_book_genre")
    login_url = reverse_lazy('login')
    template_name = 'book_reference/create_genre.html'

class UpdateGenre(PermissionRequiredMixin, LoginRequiredMixin,generic.UpdateView):
    model = models.BookGenre
    form_class = forms.GenreForm
    permission_required = ("book_reference.change_book_genre")
    login_url = reverse_lazy('login')
    template_name = 'book_reference/update_genre.html'

class ShowGenre(PermissionRequiredMixin, LoginRequiredMixin,generic.DetailView):
    model = models.BookGenre
    permission_required = ("book_reference.view_book_genre")
    login_url = reverse_lazy('login')
    template_name = 'book_reference/detail_genre.html'

class ShowGenres(PermissionRequiredMixin, LoginRequiredMixin, generic.ListView):
    model = models.BookGenre
    permission_required = ("book_reference.view_book_genre")
    login_url = reverse_lazy('login')
    template_name = 'book_reference/list_genres.html'

class DeleteGenre(PermissionRequiredMixin, LoginRequiredMixin,generic.DeleteView):
    model = models.BookGenre
    permission_required = ("book_reference.delete_book_genre")
    login_url = reverse_lazy('login')
    template_name = 'book_reference/delete_genre.html'
    success_url="/refs/genres-show"


class CreateAuthor(PermissionRequiredMixin, LoginRequiredMixin,generic.CreateView):
    model = models.BookAuthor
    permission_required = ("book_reference.add_book_author")
    login_url = reverse_lazy('login')
    form_class = forms.AuthorForm
    template_name = 'book_reference/create_author.html'

class UpdateAuthor(PermissionRequiredMixin, LoginRequiredMixin,generic.UpdateView):
    model = models.BookAuthor
    form_class = forms.AuthorForm
    permission_required = ("book_reference.change_book_author")
    login_url = reverse_lazy('login')
    template_name = 'book_reference/update_author.html'

class ShowAuthor(PermissionRequiredMixin, LoginRequiredMixin,generic.DetailView):
    model = models.BookAuthor
    permission_required = ("book_reference.view_book_author")
    login_url = reverse_lazy('login')
    template_name = 'book_reference/detail_author.html'

class ShowAuthors(PermissionRequiredMixin, LoginRequiredMixin,generic.ListView):
    model = models.BookAuthor
    permission_required = ("book_reference.view_book_author")
    login_url = reverse_lazy('login')
    template_name = 'book_reference/list_authors.html'

class DeleteAuthor(PermissionRequiredMixin, LoginRequiredMixin,generic.DeleteView):
    model = models.BookAuthor
    permission_required = ("book_reference.delete_book_author")
    login_url = reverse_lazy('login')
    template_name = 'book_reference/delete_author.html'
    success_url="/refs/authors-show"


class CreatePublisher(PermissionRequiredMixin, LoginRequiredMixin,generic.CreateView):
    model = models.BookPublisher
    form_class = forms.PublisherForm
    permission_required = ("book_reference.add_book_publisher")
    login_url = reverse_lazy('login')
    template_name = 'book_reference/create_publisher.html'

class UpdatePublisher(PermissionRequiredMixin, LoginRequiredMixin,generic.UpdateView):
    model = models.BookPublisher
    form_class = forms.PublisherForm
    permission_required = ("book_reference.change_book_publisher")
    login_url = reverse_lazy('login')   
    template_name = 'book_reference/update_publisher.html'

class ShowPublisher(PermissionRequiredMixin, LoginRequiredMixin,generic.DetailView):
    model = models.BookPublisher
    permission_required = ("book_reference.view_book_publisher")
    login_url = reverse_lazy('login')    
    template_name = 'book_reference/detail_publisher.html'

class ShowPublishers(PermissionRequiredMixin, LoginRequiredMixin,generic.ListView):
    model = models.BookPublisher
    permission_required = ("book_reference.view_book_publisher")
    login_url = reverse_lazy('login')
    template_name = 'book_reference/list_publishers.html'

class DeletePublisher(PermissionRequiredMixin, LoginRequiredMixin,generic.DeleteView):
    model = models.BookPublisher
    permission_required = ("book_reference.delete_book_publisher")
    login_url = reverse_lazy('login')    
    template_name = 'book_reference/delete_publisher.html'
    success_url="/refs/publishers-show"


class CreateSeries(PermissionRequiredMixin, LoginRequiredMixin,generic.CreateView):
    model = models.BookSeries
    form_class = forms.SeriesForm
    permission_required = ("book_reference.add_book_series")
    login_url = reverse_lazy('login')    
    template_name = 'book_reference/create_series.html'

class UpdateSeries(PermissionRequiredMixin, LoginRequiredMixin,generic.UpdateView):
    model = models.BookSeries
    form_class = forms.SeriesForm
    permission_required = ("book_reference.change_book_series")
    login_url = reverse_lazy('login')  
    template_name = 'book_reference/update_series.html'

class ShowSeries(PermissionRequiredMixin, LoginRequiredMixin,generic.DetailView):
    model = models.BookSeries
    permission_required = ("book_reference.view_book_series")
    login_url = reverse_lazy('login')  
    template_name = 'book_reference/detail_series.html'

class ShowSeriesAll(PermissionRequiredMixin, LoginRequiredMixin,generic.ListView):
    model = models.BookSeries
    permission_required = ("book_reference.view_book_series")
    login_url = reverse_lazy('login')
    template_name = 'book_reference/list_series_all.html'

class DeleteSeries(PermissionRequiredMixin, LoginRequiredMixin,generic.DeleteView):
    model = models.BookSeries
    permission_required = ("book_reference.view_book_series")
    login_url = reverse_lazy('login')  
    template_name = 'book_reference/delete_series.html'
    success_url="/refs/series-all-show"  
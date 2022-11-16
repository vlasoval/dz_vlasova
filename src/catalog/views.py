from django.shortcuts import render
from django.views import generic
from book_reference import models
from book import models as b_models
from django.db.models import Q

from home_page.views import BaseTemplatePageMixin


# Create your views here.
class Catalogs(BaseTemplatePageMixin, generic.ListView):
    model = models.BookGenre
    template_name='catalog/catalogs.html'

class Catalog(BaseTemplatePageMixin, generic.TemplateView):
    template_name='catalog/catalog.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['book_filter'] = b_models.Book.objects.filter(book_genre__pk=kwargs['pk'])
        context['current_genre'] = models.BookGenre.objects.get(pk=kwargs['pk'])
        return context

class Search(BaseTemplatePageMixin, generic.TemplateView):
    template_name='catalog/search.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        search=self.request.GET['search']
        context['search_b'] = b_models.Book.objects.filter(Q(book_title__icontains=search) | Q(book_author__name__icontains=search))

        return context        
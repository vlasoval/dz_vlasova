from django.shortcuts import render
from django.views import generic
from book_reference import models
from book import models as b_models

# Create your views here.
class Catalogs(generic.ListView):
    model = models.BookGenre
    template_name='catalog/catalogs.html'

class Catalog(generic.TemplateView):
    template_name='catalog/catalog.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['book_filter'] = b_models.Book.objects.filter(book_genre__pk=kwargs['pk'])
        context['current_genre'] = models.BookGenre.objects.get(pk=kwargs['pk'])
        return context

# class CatalogRom(generic.TemplateView):
#     template_name='catalog/catalogs.html'
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args,**kwargs)
#         context['book_filter'] = b_models.Book.objects.filter(book_genre__name='Романы')
#         return context

# class CatalogHist(generic.TemplateView):
#     template_name='catalog/catalogs.html'
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args,**kwargs)
#         context['book_filter'] = b_models.Book.objects.filter(book_genre__name='Историческая литература')
#         return context  

# class CatalogFant(generic.TemplateView):
#     template_name='catalog/catalogs.html'
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args,**kwargs)
#         context['book_filter'] = b_models.Book.objects.filter(book_genre__name='Фантастика')
#         return context     

# class CatalogBio(generic.TemplateView):
#     template_name='catalog/catalogs.html'
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args,**kwargs)
#         context['book_filter'] = b_models.Book.objects.filter(book_genre__name='Биографии')
#         return context      

# class CatalogChild(generic.TemplateView):
#     template_name='catalog/catalogs.html'
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args,**kwargs)
#         context['book_filter'] = b_models.Book.objects.filter(book_genre__name='Детские книги')
#         return context                          
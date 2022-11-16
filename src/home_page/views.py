from django.shortcuts import render
from django.views import generic
from book import models as b_models
from book_reference import models
# Create your views here.

class BaseTemplatePageMixin:
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['current_genre_all'] = models.BookGenre.objects.all()

        return context

class HomePage(BaseTemplatePageMixin, generic.TemplateView):
    template_name='home_page/home_page.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['new_book'] = b_models.Book.objects.order_by('-book_date')
        context['best_book'] = b_models.Book.objects.order_by('book_rating')
        context['ref_book'] = b_models.Book.objects.order_by('book_count')
        
        return context

class Delivery(BaseTemplatePageMixin, generic.TemplateView):
    template_name='home_page/delivery.html'

class Payment(BaseTemplatePageMixin, generic.TemplateView):
    template_name='home_page/payment.html'

class Contacts(BaseTemplatePageMixin, generic.TemplateView):
    template_name='home_page/contacts.html'
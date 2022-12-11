from django.shortcuts import render
from django.views import generic
from book import models as b_models
from book_reference import models
import requests
import time
# Create your views here.

class BaseTemplatePageMixin:
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['current_genre_all'] = models.BookGenre.objects.all()

        current_time_in_seconds = time.time()
        one_day_in_seconds = 60*60*24
        currency_rate = self.request.session.get('currency_rate', None)
        currency_rate_updated = self.request.session.get('currency_rate_updated', current_time_in_seconds)

        if not currency_rate or (current_time_in_seconds - currency_rate_updated) > one_day_in_seconds:
            try:
                headers = {'Accept': 'application/json'}
                r = requests.get('https://www.nbrb.by/api/exrates/rates/431', headers=headers, timeout=1)
                currency_object = r.json()
                currency_rate = currency_object['Cur_OfficialRate']
            except:
                currency_rate = 2.5
                
            self.request.session['currency_rate'] = currency_rate
            self.request.session['currency_rate_updated'] = time.time()

        context['currency'] = currency_rate
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

class AdminPortal(BaseTemplatePageMixin, generic.TemplateView):
    template_name='home_page/admin_portal.html'
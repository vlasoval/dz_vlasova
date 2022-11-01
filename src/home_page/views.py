from django.shortcuts import render
from django.views import generic
from book import models as b_models
# Create your views here.

class HomePage(generic.TemplateView):
    template_name='home_page/home_page.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['a_book'] = b_models.Book.objects.get(pk=1)
        return context
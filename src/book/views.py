from django.views import generic
from . import models

from home_page.views import BaseTemplatePageMixin


class ShowBook(BaseTemplatePageMixin, generic.DetailView):
    model = models.Book
    template_name = 'book/detail_book.html'

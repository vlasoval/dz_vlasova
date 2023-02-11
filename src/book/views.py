from django.views import generic
from . import models,forms
from book_reference import models as b_models
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from home_page.views import BaseTemplatePageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


class ShowBook(BaseTemplatePageMixin, generic.DetailView):
    model = models.Book
    template_name = 'book/detail_book.html'

class CreateBookComments(BaseTemplatePageMixin, LoginRequiredMixin, generic.CreateView):
    model = models.BookComments
    login_url = reverse_lazy('login')
    form_class = forms.BookCommentsForm
    template_name = 'book/create_book_comment.html'

    def get_form_kwargs(self):
        kw = super().get_form_kwargs()
        kw['user'] = self.request.user
        kw['book_pk'] = self.kwargs.get('pk')
        return kw

    def form_valid(self, form):
        book_pk = self.kwargs.get('pk')
        book = models.Book.objects.get(pk=book_pk)
        form.instance.book = book
        form.instance.customer = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('book:book-detail', kwargs={'pk': self.object.book.pk})

class ShowComments(BaseTemplatePageMixin, generic.ListView):
    paginate_by = 7
    model = models.BookComments
    template_name = 'book/comments_list.html'
    class Meta:
        ordering = ['-id']
    def get_queryset(self): 
        qs = super().get_queryset() 
        if 'search' in self.request.GET:
            search=self.request.GET['search']
            return qs.filter(comment__icontains=search)
        else:
            return qs

# class SearchCom(BaseTemplatePageMixin, generic.TemplateView):
#     template_name='book/search_com.html'
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args,**kwargs)
#         search=self.request.GET['search']
#         context['search_c'] = models.BookComments.objects.filter(comment__icontains=search
#         )
#         return context  

class UpdateBookComments(BaseTemplatePageMixin, LoginRequiredMixin, generic.UpdateView):
    model = models.BookComments
    form_class = forms.BookCommentsFormUpdate
    template_name = 'book/update_book_comment.html'
    login_url = reverse_lazy('login')
    def get_success_url(self):
        return reverse_lazy('book:book-detail', kwargs={'pk': self.object.book.pk})        


class DeleteBookComments(BaseTemplatePageMixin, LoginRequiredMixin, generic.DeleteView):
    model = models.BookComments
    template_name = 'book/delete_book_comment.html'
    login_url = reverse_lazy('login')
    def get_success_url(self):
        return reverse_lazy('book:book-detail', kwargs={'pk': self.object.book.pk})

class ShowBooks(BaseTemplatePageMixin, generic.ListView):
    model = models.Book
    template_name = 'book/book_list.html'

class CreateBook(BaseTemplatePageMixin, PermissionRequiredMixin, LoginRequiredMixin, generic.CreateView):
    model = models.Book
    form_class = forms.BookForm
    template_name = 'book/create_book.html'
    permission_required = ("book.add_book")
    login_url = reverse_lazy('login')
    def get_success_url(self):
        return reverse_lazy('book:book-detail', kwargs={'pk': self.object.pk})


class UpdateBook(BaseTemplatePageMixin, PermissionRequiredMixin, LoginRequiredMixin, generic.UpdateView):
    model = models.Book
    form_class = forms.BookForm
    template_name = 'book/update_book.html'
    permission_required = ("book.change_book")
    login_url = reverse_lazy('login')
    def get_success_url(self):
        return reverse_lazy('book:book-detail', kwargs={'pk': self.object.pk})


def handle_uploaded_file(f):
    file_content = f.read().decode("utf-8")
    for line in file_content.split('\n'):
        fields = line.split(',')
        book = models.Book(
            book_title=fields[0],
            book_cover_photo=fields[1],
            book_publisher=b_models.BookPublisher.objects.get(pk=int(fields[3])),
            book_series=b_models.BookSeries.objects.get(pk=int(fields[4])),            
            book_price=float(fields[6]),
            book_year=int(fields[7]),
            book_page=int(fields[8]),
            book_cover=fields[9],
            book_format=fields[10],
            book_isbn=fields[11],
            book_weight=int(fields[12]),
            book_age=fields[13],
            book_count=int(fields[14]),
            book_active=fields[15],
            book_rating=float(fields[16]),
        )
        book.save()
        book.book_genre.add(b_models.BookGenre.objects.get(pk=int(fields[2])))
        book.book_author.add(b_models.BookAuthor.objects.get(pk=int(fields[5])))

def upload_file(request):
    if request.method == 'POST':
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return redirect('home-page')
    else:
        form = forms.UploadFileForm()
    return render(request, 'book/create_book_cvs.html', {'form': form})
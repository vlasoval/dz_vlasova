from django.urls import path
from . import views
app_name = 'book'
urlpatterns = [
    path('show/<int:pk>/', views.ShowBook.as_view(), name='book-detail'),
    path('add_book_comment/<int:pk>/', views.CreateBookComments.as_view(), name='book-comment'),
    path('update_book_comment/<int:pk>/', views.UpdateBookComments.as_view(), name='book-comment-update'),
    path('delete_book_comment/<int:pk>/', views.DeleteBookComments.as_view(), name='book-comment-delete'),
    path('all/', views.ShowBooks.as_view(), name='book-list'),
    path('add_book/', views.CreateBook.as_view(), name='book-add'),
    path('update_book/<int:pk>/', views.UpdateBook.as_view(), name='book-update'),
    path('add_book_csv/', views.upload_file, name='book-add-csv'),
]
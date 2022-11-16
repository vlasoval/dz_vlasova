from django.urls import path
from . import views
app_name = 'book'
urlpatterns = [
    path('show/<int:pk>/', views.ShowBook.as_view(), name='book-detail'),
]
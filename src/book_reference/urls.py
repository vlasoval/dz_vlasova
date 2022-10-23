from django.urls import path
from . import views
app_name = 'book_reference'
urlpatterns = [
    path('genre-create/', views.CreateGenre.as_view(), name='genre-create'),
    path('genre-update/<int:pk>/', views.UpdateGenre.as_view(), name='genre-update'),
    path('genre-delete/<int:pk>/', views.DeleteGenre.as_view(), name='genre-delete'),
    path('genre-show/<int:pk>/', views.ShowGenre.as_view(), name='genre-detail'),
    path('genres-show/', views.ShowGenres.as_view(), name='genre-list'),
    path('author-create/', views.CreateAuthor.as_view(), name='author-create'),
    path('author-update/<int:pk>/', views.UpdateAuthor.as_view(), name='author-update'),
    path('author-delete/<int:pk>/', views.DeleteAuthor.as_view(), name='author-delete'),
    path('author-show/<int:pk>/', views.ShowAuthor.as_view(), name='author-detail'),
    path('authors-show/', views.ShowAuthors.as_view(), name='author-list'),
    path('publisher-create/', views.CreatePublisher.as_view(), name='publisher-create'),
    path('publisher-update/<int:pk>/', views.UpdatePublisher.as_view(), name='publisher-update'),
    path('publisher-delete/<int:pk>/', views.DeletePublisher.as_view(), name='publisher-delete'),
    path('publisher-show/<int:pk>/', views.ShowPublisher.as_view(), name='publisher-detail'),
    path('publishers-show/', views.ShowPublishers.as_view(), name='publisher-list'),
    path('series-create/', views.CreateSeries.as_view(), name='series-create'),
    path('series-update/<int:pk>/', views.UpdateSeries.as_view(), name='series-update'),
    path('series-delete/<int:pk>/', views.DeleteSeries.as_view(), name='series-delete'),
    path('series-show/<int:pk>/', views.ShowSeries.as_view(), name='series-detail'),
    path('series-all-show/', views.ShowSeriesAll.as_view(), name='series-list'),
]
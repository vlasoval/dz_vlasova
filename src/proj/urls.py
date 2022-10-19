"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from book_reference import views as br_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genre_create/', br_views.CreateGenre.as_view()),
    path('genre_update/<int:pk>/', br_views.UpdateGenre.as_view()),
    path('genre_delete/<int:pk>/', br_views.DeleteGenre.as_view()),
    path('genre_show/<int:pk>/', br_views.ShowGenre.as_view()),
    path('genres_show/', br_views.ShowGenres.as_view()),
    path('author_create/', br_views.CreateAuthor.as_view()),
    path('author_update/<int:pk>/', br_views.UpdateAuthor.as_view()),
    path('author_delete/<int:pk>/', br_views.DeleteAuthor.as_view()),
    path('author_show/<int:pk>/', br_views.ShowAuthor.as_view()),
    path('authors_show/', br_views.ShowAuthors.as_view()),
    path('publisher_create/', br_views.CreatePublisher.as_view()),
    path('publisher_update/<int:pk>/', br_views.UpdatePublisher.as_view()),
    path('publisher_delete/<int:pk>/', br_views.DeletePublisher.as_view()),
    path('publisher_show/<int:pk>/', br_views.ShowPublisher.as_view()),
    path('publishers_show/', br_views.ShowPublishers.as_view()),
    path('series_create/', br_views.CreateSeries.as_view()),
    path('series_update/<int:pk>/', br_views.UpdateSeries.as_view()),
    path('series_delete/<int:pk>/', br_views.DeleteSeries.as_view()),
    path('series_show/<int:pk>/', br_views.ShowSeries.as_view()),
    path('series_all_show/', br_views.ShowSeriesAll.as_view()),
]

from django.urls import path
from . import views
app_name = 'catalog'
urlpatterns = [
    path('',views.Catalogs.as_view(), name='catalog'),
    path('<int:pk>/',views.Catalog.as_view(), name='catalogs')
]
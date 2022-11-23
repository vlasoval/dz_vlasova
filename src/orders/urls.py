from django.urls import path
from . import views
app_name = 'orders'
urlpatterns = [
    path('cart', views.show_cart, name='show-cart'),
]
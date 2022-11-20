from django.urls import path
from . import views
app_name = 'orders'
urlpatterns = [
    path('cart', views.ViewCart.as_view(), name='show-cart'),
]
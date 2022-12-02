from django.urls import path
from . import views
app_name = 'orders'
urlpatterns = [
    path('cart', views.show_cart, name='show-cart'),
    path('del-position/<int:pk>/', views.DelPosition.as_view(), name='del-position'),
    path('create-order/', views.Order.as_view(), name='create-order'),
    path('success/', views.OrderSuccess.as_view(), name='order-success'),    
]
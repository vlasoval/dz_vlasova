from django.urls import path
from . import views
app_name = 'orders'
urlpatterns = [
    path('cart', views.show_cart, name='show-cart'),
    path('del-position/<int:pk>/', views.DelPosition.as_view(), name='del-position'),
    path('create-order/', views.Order.as_view(), name='create-order'),
    path('success/<int:pk>/', views.OrderSuccess.as_view(), name='order-success'),
    path('all/', views.OrdersAll.as_view(), name='list-orders'),
    path('current/', views.OrdersUser.as_view(), name='orders-user'),
    path('update/<int:pk>/', views.OrderUpdate.as_view(), name='order-update'),
    path('update-com/<int:pk>/', views.OrderCommentUpdate.as_view(), name='com-update'),
    path('detail/<int:pk>/', views.OrderDetail.as_view(), name='order-detail'),
    path('delete/<int:pk>/', views.OrderDelete.as_view(), name='order-delete'),     
]
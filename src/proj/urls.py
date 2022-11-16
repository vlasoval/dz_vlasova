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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home_page import views
from catalog import views as c_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('refs/', include('book_reference.urls', namespace='book_reference')),
    path('',views.HomePage.as_view(), name='home-page'),
    path('catalog/',include('catalog.urls', namespace='catalog')),
    path('delivery/',views.Delivery.as_view(), name='delivery'),
    path('payment/',views.Payment.as_view(), name='payment'),
    path('contacts/',views.Contacts.as_view(), name='contacts'),
    path('search/', c_views.Search.as_view(template_name='catalog/search.html'), name='search'),
    path('book/', include('book.urls', namespace='book')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from . import models

class CartAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user')
class BookInCartAdmin (admin.ModelAdmin):
    list_display = ('pk', 'book', 'cart', 'quantity', 'created_date', 'updated_date')
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'status','cart','last_first_name','email','adress','phone_number','created_date', 'updated_date')    

admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.BookInCart, BookInCartAdmin)
admin.site.register(models.Order, OrderAdmin)
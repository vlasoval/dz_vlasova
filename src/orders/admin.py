from django.contrib import admin
from . import models

class CartAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user')


admin.site.register(models.Cart, CartAdmin)
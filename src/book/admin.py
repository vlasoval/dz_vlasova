from . import models
from django.contrib import admin

# # Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('pk', 'book_title', 'book_publisher')


admin.site.register(models.Book, BookAdmin)
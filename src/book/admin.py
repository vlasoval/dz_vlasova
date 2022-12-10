from . import models
from django.contrib import admin

# # Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('pk', 'book_title', 'book_date', 'book_date_change')
class BookCommentsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'customer', 'rating', 'created_date','updated_date')


admin.site.register(models.Book, BookAdmin)
admin.site.register(models.BookComments, BookCommentsAdmin)
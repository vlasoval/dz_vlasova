from django.contrib import admin
from . import models

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk','user','birthday_date')    

admin.site.register(models.Profile, ProfileAdmin)
from django.db import models
from django.contrib.auth.models import Group, Permission


managers = Group.objects.get_or_create(name='Managers')
customers = Group.objects.get_or_create(name='Customers')






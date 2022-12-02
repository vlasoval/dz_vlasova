from django.db import models
from django.contrib.auth.models import Group

managers = Group.objects.get_or_create(name='Managers')
customers = Group.objects.get_or_create(name='Customers')


from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)   
    phone_number = models.CharField(max_length=30, blank=True)
    birthday_date = models.DateField(null=True, blank=True,)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=20)
    address1 = models.CharField(max_length=20)
    address2 = models.CharField(max_length=20)
    information = models.TextField(blank=True, null=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    Profile.objects.get_or_create(user=instance)
    instance.profile.save()



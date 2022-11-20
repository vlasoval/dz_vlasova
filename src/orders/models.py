from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='carts',
        verbose_name='User Cart',
        null=True,
        blank=True,
    )

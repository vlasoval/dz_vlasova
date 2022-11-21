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

class BookInCart(models.Model):
    book = models.ForeignKey(
        "book.Book",
        verbose_name='Book in a cart',
        on_delete=models.PROTECT)
    cart = models.ForeignKey(
        "orders.Cart",
        verbose_name='Cart',
        related_name='books',
        on_delete=models.PROTECT)
    quantity = models.IntegerField(
        verbose_name='Quantity',
        default=1)
    created_date = models.DateTimeField(
        'Created date',
        auto_now=False,
        auto_now_add=True)      
    updated_date = models.DateTimeField(
        'Updated date',
        auto_now=True,
        auto_now_add=False)  
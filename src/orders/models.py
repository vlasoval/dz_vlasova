from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

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
    def total_price(self):
        all_books_positions = self.books.all()
        total_price = 0
        for book_position in all_books_positions:
            total_price += book_position.price_per_position
        return total_price

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


    @property    
    def price_per_position(self):
        return self.book.book_price * self.quantity
statuses=(
    ('accepted', 'Заказ принят'),
    ('collected', 'Заказ собран'),
    ('sent', 'Заказ отправлен'),
    ('deliver', 'Заказ доставлен'),    
)
class Order(models.Model):
    status = models.CharField(
        verbose_name='Статус',
        max_length=200,
        choices=statuses,
        default='Заказ принят'
    )
    cart = models.OneToOneField(
        "orders.Cart",
        verbose_name='Cart',
        related_name='order',
        on_delete=models.PROTECT)   
    last_first_name=models.CharField(
        max_length=200,
        verbose_name='Фамилия Имя:'
    )
    email=models.EmailField(
        max_length=200,
        verbose_name='E-mail:'
    )
    adress=models.CharField(
        max_length=200,
        verbose_name='Адрес достаки:'
    )
    phone_number=models.CharField(
        max_length=200,
        verbose_name='Номер телефона:'
    )
    information=models.TextField(
        verbose_name='Добавить комментарий к заказу:',
        null=True,
        blank=True,
    )
    created_date = models.DateTimeField(
        'Created date',
        auto_now=False,
        auto_now_add=True)      
    updated_date = models.DateTimeField(
        'Updated date',
        auto_now=True,
        auto_now_add=False)
    def get_absolute_url(self):
        return reverse_lazy('orders:order-success', kwargs={'pk':self.pk})        

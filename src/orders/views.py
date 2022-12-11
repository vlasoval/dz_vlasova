from django.shortcuts import render
from . import models, forms
from book import models as book_models
from django.views import generic
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

class DelPosition(generic.DeleteView):
    model = models.BookInCart
    success_url = reverse_lazy('orders:show-cart')
    template_name='orders/position_delete.html'
def show_cart(request):
    context = {}
    context['cart'] = None
    if request.method == 'POST':
        book_pk = request.POST.get('book_pk')
        quantity = request.POST.get('quantity')
        if book_pk and quantity:
            cart_id = request.session.get('cart_id', 0)
            if request.user.is_authenticated:
                user = request.user
            else:
                user = None
            if cart_id == 0:
                cart_id=None    
            cart, created = models.Cart.objects.get_or_create(
                pk=cart_id,
                defaults={'user':user}
                )
            context['cart'] = cart    
            if created:
                request.session['cart_id'] = cart.pk
            book = book_models.Book.objects.get(pk=book_pk)
            book_in_a_cart, created = models.BookInCart.objects.get_or_create(
                book=book,
                cart=cart,
                defaults={
                    'quantity':quantity,
                }              
            )
            if not created:
                book_in_a_cart.quantity=book_in_a_cart.quantity+int(quantity)
                book_in_a_cart.save()
    else:            
        cart_id = request.session.get('cart_id')
        if cart_id:
            cart = models.Cart.objects.get(pk=cart_id)
            context['cart'] = cart
    if request.user.is_authenticated:
        context['form'] = forms.OrderForm(initial={'last_first_name' : request.user.last_name+' '+request.user.first_name,\
            'email': request.user.email,\
            'adress': request.user.profile.address1,\
            'phone_number': request.user.profile.phone_number})       
    else:
        context['form'] = forms.OrderForm()

    return render(
        request=request, 
        template_name='orders/view_cart.html', 
        context=context)

User = get_user_model()
class Order(generic.CreateView):
    model=models.Order
    form_class=forms.OrderForm
    def form_valid(self, form):
        cart = models.Cart.objects.get(pk=self.request.session.get('cart_id'))
        form.instance.cart=cart
        return super().form_valid(form)
    def get_success_url(self):
        send_mail(
            'Заказ в магазине',
            'Заказ передан в обработку',
            'vlasova66666666@gmail.com',
            [user.email for user in User.objects.filter(groups__name='Managers')],
            fail_silently=False,
        )
        del self.request.session['cart_id']
        orderid=self.object.pk
        return reverse_lazy('orders:order-success', kwargs={'pk': orderid})

class OrderSuccess(generic.DetailView):
    model = models.Order
    template_name='orders/success_order.html'

class OrdersAll(generic.ListView):
    model = models.Order
    # permission_required = ("accounts.view_book_genre")
    # login_url = reverse_lazy('login')
    template_name = 'orders/list_orders.html'

class OrdersUser(generic.ListView):
    model = models.Order
    # permission_required = ("accounts.view_book_genre")
    # login_url = reverse_lazy('login')
    template_name = 'orders/list_orders.html'    
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args,**kwargs)      
        return queryset.filter(cart__user__pk=self.request.user.pk)
class OrderDetail(generic.DetailView):
    model = models.Order
    template_name = 'orders/order_detail.html'

class OrderUpdate(generic.UpdateView):
    model = models.Order
    form_class = forms.OrderUpdateForm
    template_name = 'orders/update_orders.html'
    def get_success_url(self):
        return reverse_lazy('orders:order-detail', kwargs={'pk': self.object.pk})

class OrderCommentUpdate(generic.UpdateView):
    model = models.Order
    form_class = forms.CommentUpdateForm
    template_name = 'orders/update_orders.html'
    def get_success_url(self):
        return reverse_lazy('orders:order-detail', kwargs={'pk': self.object.pk})

class OrderDelete(generic.DeleteView):
    model = models.Order
    template_name='orders/order_delete.html'
    def get_success_url(self):
        return reverse_lazy('orders:orders-user')




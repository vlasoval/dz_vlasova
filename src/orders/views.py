from django.shortcuts import render
from . import models, forms
from book import models as book_models
from django.views import generic
from django.urls import reverse_lazy

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
    context['form'] = forms.OrderForm()
    return render(
        request=request, 
        template_name='orders/view_cart.html', 
        context=context)

class Order(generic.CreateView):
    template_name='orders/create_order.html'
    model=models.Order
    form_class=forms.OrderForm
    success_url=reverse_lazy('orders:order-success')
    def form_valid(self, form):
        cart = models.Cart.objects.get(pk=self.request.session.get('cart_id'))
        form.instance.cart=cart
        return super().form_valid(form)
    def get_success_url(self):
        print(self.request.session['cart_id'])
        del self.request.session['cart_id']
        return super().get_success_url()

class OrderSuccess(generic.TemplateView):
    template_name='orders/success_order.html'

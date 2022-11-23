# from django.views import generic

# class ViewCart(generic.TemplateView):
#     template_name = 'orders/view_cart.html'

from django.shortcuts import render
from . import models
from book import models as book_models

def show_cart(request):
    context = {}
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
            if created:
                request.session['cart_id'] = cart.pk
            book = book_models.Book.objects.get(pk=book_pk)
            book_in_a_cart = models.BookInCart.objects.create(
                book=book,
                cart=cart,
                quantity=quantity,
            )

    return render(
        request=request, 
        template_name='orders/view_cart.html', 
        context=context)

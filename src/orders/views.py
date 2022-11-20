from django.views import generic

class ViewCart(generic.TemplateView):
    template_name = 'orders/view_cart.html'

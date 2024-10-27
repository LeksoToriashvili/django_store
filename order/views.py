from django.db.models import Sum
from django.template.context_processors import request
from django.views.generic import ListView
from order.models import CartItem, Cart

from django.shortcuts import render


class CartListView(ListView):
    model = CartItem
    template_name = 'cart.html'
    context_object_name = 'cart_items'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['user'] = user
        subtotal = sum([item.product.price*item.quantity for item in self.get_queryset()])
        context['subtotal'] = subtotal
        context['shipping'] = 3
        context['total'] = subtotal + 3
        return context

    def get_queryset(self):
        user = self.request.user
        cart = Cart.objects.filter(user=user).prefetch_related('items').first()
        cart_items = cart.items.all() if cart else []
        return cart_items

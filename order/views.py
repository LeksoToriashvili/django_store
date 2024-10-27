from django.views.generic import ListView
from order.models import CartItem

from django.shortcuts import render


class CartListView(ListView):
    model = CartItem
    template_name = 'cart.html'
    context_object_name = 'cart_items'

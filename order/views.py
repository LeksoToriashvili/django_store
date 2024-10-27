from http.client import HTTPResponse

from django.db.models import Sum
from django.http import JsonResponse, HttpResponseRedirect
from django.template.context_processors import request
from django.views.generic import ListView, View
from order.models import CartItem, Cart

from django.shortcuts import render, get_object_or_404

from store.models import Product


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


class AddToCartView(View):
    def post(self, request, *args, **kwargs):
        # Get the product ID and quantity from the form
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))  # Default to 1 if not provided

        # Retrieve the cart for the current user
        cart, created = Cart.objects.get_or_create(user=request.user)

        # Get the product object
        product = get_object_or_404(Product, id=product_id)

        # Check if the CartItem already exists
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if quantity > 0:
            if not created:
                # If it exists, update the quantity
                cart_item.quantity += quantity
            else:
                # If it's a new item, set the quantity
                cart_item.quantity = quantity
            cart_item.save()
        else:
            # If quantity is zero, delete the CartItem
            if not created:
                cart_item.delete()

        # Redirect to the current URL or another page after adding/removing from cart
        return HttpResponseRedirect(request.POST.get('current_url', '/'))


class CheckoutView(CartListView):
    template_name = 'checkout.html'

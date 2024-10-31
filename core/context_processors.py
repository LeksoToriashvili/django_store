from order.models import Cart


def cart_items_number(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).prefetch_related('items').first()
        count = cart.items.count()
    else:
        count = 0
    return {'cart_items_number': count}

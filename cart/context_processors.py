from .models import CartItem
from .cart import Cart
from django.db.models import Sum


def cart_count(request):
    if request.user.is_authenticated:
        count = CartItem.objects.filter(user=request.user).aggregate(total=Sum('quantity'))['total'] or 0
    else:
        cart = Cart(request)
        count = cart.get_item_count()
    """print(f"Cart count: {count}")"""
    return {'item_total': count}

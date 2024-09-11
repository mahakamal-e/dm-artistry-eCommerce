from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db import transaction, IntegrityError
from shop.models import Product
from .models import CartItem
from .cart import Cart

# For authenticated users only
@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def add_to_cart(request, product_id):
    
    product = get_object_or_404(Product, id=product_id)
    
    try:
        with transaction.atomic():
            cart_item, created = CartItem.objects.get_or_create(
                product=product,
                user=request.user,
                defaults={'quantity': 1}
            )
            if not created:
                cart_item.quantity += 1
                cart_item.save()
    except IntegrityError:
        # Handle exception (e.g., log error)
        pass

    return redirect('view_cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('view_cart')


def cart_count(request):
    if request.user.is_authenticated:
        # Get total count of items (including quantities) for authenticated users
        count = CartItem.objects.filter(user=request.user).aggregate(total=Sum('quantity'))['total'] or 0
    else:
        # For anonymous users, get item count from session
        cart = Cart(request)
        count = cart.get_item_count()  # Use get_item_count to get total items
    return {'item_total': count}

def add_to_cart_anon(request, product_id):
    cart = Cart(request)
    cart.add(product_id, quantity=1)
    return redirect('view_cart_anon')

def remove_from_cart_anon(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)
    return redirect('view_cart_anon')

def view_cart_anon(request):
    cart = Cart(request)
    cart_items = cart.get_items()  # Ensure this returns a list with 'product_id'
    total_price = cart.get_total_price()
    return render(request, 'cart/cart_anon.html', {'cart_items': cart_items, 'total_price': total_price})

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db import transaction, IntegrityError
from shop.models import Product
from .models import CartItem
from .cart import Cart
from django.db.models import Sum

# For authenticated users only
@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items.exists():
        return redirect('empty_cart')
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
        pass

    return redirect('view_cart')

@login_required
def remove_from_cart(request, item_id):
    try:
        # Attempt to retrieve the CartItem
        cart_item = CartItem.objects.get(id=item_id, user=request.user)
    except CartItem.DoesNotExist:
        # If the CartItem does not exist, handle the error
        return redirect('empty_cart')  # Redirect to the empty cart page or another relevant page

    # Delete the CartItem
    cart_item.delete()

    # Check if the cart is empty after removal
    if not CartItem.objects.filter(user=request.user).exists():
        return redirect('empty_cart')  # Redirect to the empty cart page if the cart is empty

    return redirect('view_cart')


def add_to_cart_anon(request, product_id):
    cart = Cart(request)
    cart.add(product_id, quantity=1)
    return redirect('view_cart_anon')

def view_cart_anon(request):
    cart = Cart(request)
    cart_items = cart.get_items()  # Ensure this returns a list with 'product_id'
    if not cart_items:
        return redirect('empty_cart')  # Redirect to empty cart page if cart is empty
    total_price = cart.get_total_price()
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def remove_from_cart_anon(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)

    # Check if the cart is empty after removal
    if not cart.get_items():  # Check if cart has no items left
        return redirect('empty_cart')  # Redirect to empty cart page if cart is empty

    return redirect('view_cart_anon')

def empty_cart_view(request):
    return render(request, 'cart/empty_cart.html')


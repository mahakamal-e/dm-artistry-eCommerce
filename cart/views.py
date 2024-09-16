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
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    if not cart_items.exists():
        return redirect('empty_cart')  # Redirect to the empty cart page
    
    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    
    return render(request, 'cart/cart.html', context)


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
    print(f"Attempting to remove item with ID: {item_id}")
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    
    # Check if the cart is empty after removal
    if not CartItem.objects.filter(user=request.user).exists():
        print("Cart is empty, redirecting to empty cart page.")
        return redirect('empty_cart')  # Redirect to the empty cart page
    
    print("Cart still has items, redirecting to view cart.")
    return redirect('view_cart')



def add_to_cart_anon(request, product_id):
    cart = Cart(request)
    cart.add(product_id, quantity=1)
    return redirect('view_cart_anon')

def remove_from_cart_anon(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)

    # Check if the cart is empty after remove
    if not cart.get_items():  # Ensure this returns a list or a count of items
        return redirect('empty_cart')  # Redirect to the empty cart page
    
    return redirect('view_cart_anon')

def view_cart_anon(request):
    cart = Cart(request)
    cart_items = cart.get_items()
    total_price = cart.get_total_price()
    
    if not cart_items:
        return redirect('empty_cart')  # Redirect to the empty cart page
    
    context = {
        'cart_items': cart_items,
        'total_price': total_price
        }
    return render(request, 'cart/cart.html', context)

def empty_cart_view(request):
    return render(request, 'cart/empty_cart.html')
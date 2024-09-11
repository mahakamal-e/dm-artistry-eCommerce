from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, CartItem
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.http import JsonResponse
from django.db import transaction
from django.contrib.auth.models import AnonymousUser

def product_list(request):
    products = Product.objects.all()
    
    # Filtering by category
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)

    # Sorting by price (asc or desc)
    sort_by = request.GET.get('sort', 'name')
    if sort_by == 'price_low':
        products = products.order_by('price')
    elif sort_by == 'price_high':
        products = products.order_by('-price')

    # Pagination: Show 10 products per page
    paginator = Paginator(products, 10)  # Change 10 to the number of products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()
    return render(request, 'shop/product_list.html', {
        'products': page_obj,  # Pass paginated products
        'categories': categories,
        'page_obj': page_obj,  # Pass page object for pagination controls
    })

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'shop/product_detail.html', {'product': product})

def home_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'shop/home.html', {
        'categories': categories,
        'products': products
    })



def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total_price': total_price})
 


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Use atomic transaction to ensure data integrity for logged-in users
        with transaction.atomic():
            cart_item, created = CartItem.objects.get_or_create(
                product=product,
                user=request.user,
                defaults={'quantity': 1}
            )
            if not created:
                cart_item.quantity += 1
                cart_item.save()

    else:
        # If the user is anonymous, store cart in session
        cart = request.session.get('cart', {})
        
        # If the product is already in the session cart, increase the quantity
        if str(product_id) in cart:
            cart[str(product_id)]['quantity'] += 1
        else:
            # If the product is not in the session cart, add it
            cart[str(product_id)] = {
                'product_id': product.id,
                'name': product.name,
                'price': str(product.price),  # Store price as a string to avoid serialization issues
                'quantity': 1
            }

        # Save the updated cart back to the session
        request.session['cart'] = cart

    # Redirect to view_cart page after adding the item
    return redirect('view_cart')

 
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')

@login_required
def cart_count(request):
    try:
        # For logged-in users, count items in CartItem
        cart_items = CartItem.objects.filter(user=request.user)
        count = cart_items.count()
    except Exception as e:
        count = 0  # Default to 0 if any error occurs
    return JsonResponse({'count': count})

def cart_count_unauthenticated(request):
    # For non-logged-in users, get cart count from session
    cart = request.session.get('cart', {})
    count = sum(item['quantity'] for item in cart.values())
    return JsonResponse({'count': count})
 
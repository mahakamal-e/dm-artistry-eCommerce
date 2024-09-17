from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
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


def about(request):
    return render(request, 'shop/about.html')

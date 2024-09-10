from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator

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
    return render(request, 'ecommerce/product_list.html', {
        'products': page_obj,  # Pass paginated products
        'categories': categories,
        'page_obj': page_obj,  # Pass page object for pagination controls
    })

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'ecommerce/product_detail.html', {'product': product})

def home_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'ecommerce/home.html', {
        'categories': categories,
        'products': products
    })

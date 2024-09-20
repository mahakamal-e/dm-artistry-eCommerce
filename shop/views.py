from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.core.paginator import Paginator
from .forms import ContactForm


def product_list(request):
    products = Product.objects.all()

    # Filtering by category
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)

    # Filtering by price range
    price_filter = request.GET.get('price_range')
    price_ranges = {
        'under-1000': (0, 1000),
        '1000-1500': (1000, 1500),
        '1500-2000': (1500, 2000),
        '2000-over': (2000, 3000)
    }

    if price_filter:
        if price_filter in price_ranges:
            min_price, max_price = price_ranges[price_filter]
            if max_price == 1e6:
                products = products.filter(price__gte=min_price)  # No upper limit
            else:
                products = products.filter(price__gte=min_price, price__lt=max_price)
        else:
            products = products.none()  # No products if the filter is invalid

    # Sorting by price (asc or desc)
    sort_by = request.GET.get('sort', 'name')
    if sort_by == 'price_low':
        products = products.order_by('price')
    elif sort_by == 'price_high':
        products = products.order_by('-price')

    # Pagination: Show 10 products per page
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Fetch all categories for the filter dropdown
    categories = Category.objects.all()

    # Flag to check if no products were found
    no_products_found = not products.exists()
    
    context = {
         'products': page_obj,
        'categories': categories,
        'page_obj': page_obj,
        'price_ranges': price_ranges,
        'selected_price_range': price_filter,
        'no_products_found': no_products_found,
    }

    return render(request, 'shop/product_list.html', context)


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


def contact_us(request):
    success_message = None
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            success_message = "Thank you for your message. We will get back to you soon."
            form = ContactForm()
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'success_message': success_message
        }
    
    return render(request, 'shop/contact_us.html', context )
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from .models import Order, OrderItem, PaymentMethod
from cart.models import CartItem
from accounts.models import UserProfile
from cart.cart import Cart


@login_required
def checkout(request):
    if request.method == 'POST':
        # Collect shipping information from the POST request
        phone_number = request.POST.get('phone_number', '')
        address_line1 = request.POST.get('address_line1', '')
        address_line2 = request.POST.get('address_line2', '')
        postcode = request.POST.get('postcode', '')
        state = request.POST.get('state', '')
        country = request.POST.get('country', '')
        payment_method = request.POST.get('payment_method')  # cash or credit_card

        # Create the order
        order = Order(
            user=request.user,
            phone_number=phone_number,
            address_line1=address_line1,
            address_line2=address_line2,
            postcode=postcode,
            state=state,
            country=country,
            payment_method=payment_method,
            first_name=request.user.first_name or '',
            last_name=request.user.last_name or '',
            email=request.user.email or ''
        )
        order.save()  # Save the order to generate and save the order number

        # Handle payment method
        if payment_method == 'credit_card':
            pass
        elif payment_method == 'cash':
            pass

        # Add items from the cart to the order
        cart_items = CartItem.objects.filter(user=request.user)
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        # Clear the cart
        cart_items.delete()

        # Redirect to an order confirmation page
        return redirect('order_confirmation', order_number=order.order_number)

    # If not a POST request, render the checkout page for authenticated users
    cart_items = CartItem.objects.filter(user=request.user)
    profile = UserProfile.objects.filter(user=request.user).first()
    payment_methods = PaymentMethod.objects.all()
    shipping_cost = Decimal('0.00')
    subtotal = sum(Decimal(item.product.price) * item.quantity for item in cart_items)
    total_price = subtotal + shipping_cost  # No shipping cost added

    return render(request, 'orders/checkout.html', {
        'cart_items': cart_items,
        'profile': profile,
        'payment_methods': payment_methods,
        'subtotal': subtotal,
        'shipping_cost': shipping_cost,
        'total_price': total_price
    })


def checkout_anonymous(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number', '')
        address_line1 = request.POST.get('address_line1', '')
        address_line2 = request.POST.get('address_line2', '')
        postcode = request.POST.get('postcode', '')
        state = request.POST.get('state', '')
        country = request.POST.get('country', '')
        payment_method = request.POST.get('payment_method')

        order = Order(
            phone_number=phone_number,
            address_line1=address_line1,
            address_line2=address_line2,
            postcode=postcode,
            state=state,
            country=country,
            payment_method=payment_method,
        )
        
        order.save()
        cart = Cart(request)
        cart_items = cart.get_items()
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product_id=item['product_id'],
                quantity=item['quantity'],
                price=item['price']
            )

        request.session.pop('cart_items', [])

        return redirect('order_confirmation', order_number=order.order_number)
   
    cart = Cart(request)
    cart_items = cart.get_items()
    payment_methods = PaymentMethod.objects.all()
    shipping_cost = Decimal('0.00')
    subtotal = sum(Decimal(item['price']) * item['quantity'] for item in cart_items)
    total_price = subtotal + shipping_cost

    return render(request, 'orders/checkout_anon.html', {
        'cart_items': cart_items,
        'payment_methods': payment_methods,
        'subtotal': subtotal,
        'shipping_cost': shipping_cost,
        'total_price': total_price
    })

    
def order_confirmation(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    return render(request, 'orders/order_confirmation.html', {
        'order': order
    })
    

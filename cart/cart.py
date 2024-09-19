from django.shortcuts import get_object_or_404
from shop.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product_id, quantity=1):
        product = get_object_or_404(Product, id=product_id)
        if str(product_id) in self.cart:
            self.cart[str(product_id)]['quantity'] += quantity
        else:
            self.cart[str(product_id)] = {
                'product_id': product.id,
                'name': product.name,
                'artist': product.artist,
                'price': str(product.price),
                'quantity': quantity,
                'image_url': product.image.url  # Add image URL
                
                }
    
        self.save()


    def remove(self, product_id):
        if str(product_id) in self.cart:
            del self.cart[str(product_id)]
            self.save()

    def get_items(self):
        return [
            {
                'product_id': item_data['product_id'],
                'name': item_data['name'],
                'price': item_data['price'],
                'quantity': item_data['quantity'],
                'image_url': item_data.get('image_url', '')  # Include image URL
            }
            for item_data in self.cart.values()
            ]

    def get_total_price(self):
        return sum(float(item['price']) * item['quantity'] for item in self.get_items())

    def get_item_count(self):
        return sum(item['quantity'] for item in self.cart.values())

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    def clear(self):
        # Clear the cart items from the session
        self.session.pop('cart', None)
        self.session.modified = True
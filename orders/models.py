from django.contrib.auth.models import User
from shop.models import Product
from django.db import models
from django.utils import timezone


class Order(models.Model):
    """Represents an order placed by a user or a customer"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=50, default='')  
    last_name = models.CharField(max_length=50, default='')
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    postcode = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    order_number = models.CharField(max_length=10, blank=True, unique=True, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    payment_method = models.ForeignKey('PaymentMethod', on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Override the save method to generate an order number if it is not set
        """
        if not self.order_number:
            self.order_number = self.generate_order_number()
        super().save(*args, **kwargs)

    def generate_order_number(self):
        """Generate a unique order number."""
        import uuid
        return str(uuid.uuid4().hex[:8].upper())

    def __str__(self):
        order_info = f"Order {self.order_number}"
        user_info = f"by {self.user.username if self.user else 'Customer'}"
        return f"{order_info} {user_info}"
 
  
class OrderItem(models.Model):
    """
    Represents an item within an order.
    order has how many items
    """
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"
    
    
class PaymentMethod(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


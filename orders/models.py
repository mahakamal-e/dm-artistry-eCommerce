# orders/models.py

from django.contrib.auth.models import User
from shop.models import Product
from django.db import models
from django.utils import timezone

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    postcode = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50, default='')  # Set default=''
    last_name = models.CharField(max_length=50, default='')   # Optionally, you might also want to do the same for last_name
    email = models.EmailField(null=True, blank=True)
    order_number = models.CharField(max_length=10, blank=True, unique=True, editable=False)  # Added order_number field
    created_at = models.DateTimeField(default=timezone.now)
    
    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self.generate_order_number()
        super().save(*args, **kwargs)

    def generate_order_number(self):
        import uuid
        return str(uuid.uuid4().hex[:8].upper())

    def __str__(self):
        return f"Order {self.order_number} by {self.user.username if self.user else 'Guest'}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"

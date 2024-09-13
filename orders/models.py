from django.db import models
from django.contrib.auth.models import User
from shop.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_number = models.CharField(max_length=20, unique=True, blank=True)  # Custom field

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self.generate_order_number()
        super().save(*args, **kwargs)

    def generate_order_number(self):
        """Implement order number generation using UUID"""
        import uuid
        return str(uuid.uuid4().hex[:8].upper())

    def __str__(self):
        return f"Order {self.order_number} by {self.user.username if self.user else 'Customer'}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        """ a human-readable string representation of an instance
        ex: "Artwork A (x3)"
        """
        return f"{self.product.name} (x{self.quantity})"
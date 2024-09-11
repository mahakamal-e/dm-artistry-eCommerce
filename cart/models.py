from django.db import models
from django.contrib.auth.models import User
from shop.models import Product 

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'


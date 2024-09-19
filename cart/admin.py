from django.contrib import admin
from .models import CartItem


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'date_added')
    list_filter = ('user', 'product')
    search_fields = ('user__username', 'product__name')
    ordering = ('-date_added',)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

admin.site.register(CartItem, CartItemAdmin)
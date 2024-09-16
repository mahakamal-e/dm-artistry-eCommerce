from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    """Inline admin interface for editing `OrderItem` instances"""
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity', 'price')
    # The button to add a new item is provided automatically

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'get_user', 'created_at', 'payment_method', 'phone_number', 'first_name', 'last_name', 'email')
    list_filter = ('created_at', 'payment_method', 'user')  # Add 'user' to filter by registered/guest orders
    search_fields = ('order_number', 'user__username', 'email', 'first_name', 'last_name')
    inlines = [OrderItemInline]
    readonly_fields = ('order_number', 'created_at')

    def get_user(self, obj):
        """Return the username or indicate a guest order."""
        return obj.user.username if obj.user else "Guest User"
    get_user.short_description = 'User'

    def has_delete_permission(self, request, obj=None):
        return False


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    readonly_fields = ('order', 'product', 'quantity', 'price')

from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    """
    Inline admin interface for editing `OrderItem` instance.
    Args:
        model: The model class this inline admin interface is for.
        extra: Number of empty forms to display
        Fields that should be displayed can edit.
    """
    model = OrderItem
    extra = 0
    fields = ['product', 'quantity', 'price']
    # The button to add a new item is provided automatically


class OrderAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the `Order` model.
    
    Args:
        list_display: Fields to display in the list view of orders.
        list_filter: Fields by which to filter the list of orders.
        search_fields: Fields to search in the admin search box.
        inlines: Inline admin classes to display related models.
        readonly_fields: Fields that should be displayed as read-only.
    """
    list_display = ('order_number', 'get_user', 'created_at', 'payment_method', 'phone_number', 'first_name', 'last_name', 'email')
    list_filter = ('created_at', 'payment_method', 'user')
    # Filter by creation date, payment method, and user
    search_fields = ('order_number', 'user__username', 'email', 'first_name', 'last_name')
    inlines = [OrderItemInline]
    readonly_fields = ('order_number', 'created_at')

    def get_user(self, obj):
        """
        Return the username of the user who placed the order
        if it user or customer
        Args:
            obj: The `Order` instance.
        Returns:
            str: The username or 'Guest User'.
        """
        return obj.user.username if obj.user else "Guest User"
    get_user.short_description = 'User'

    def has_delete_permission(self, request, obj=None):
        """
        Disable the delete permission for the order.
        """
        return False


class OrderItemAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the `OrderItem` model.
    """
    list_display = ('order', 'product', 'quantity', 'price')
    readonly_fields = ('order', 'product', 'quantity', 'price')


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)

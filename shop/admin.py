from django.contrib import admin
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    """Admin interface for managing `Category` models."""
    list_display = ('name', 'description')


class ProductAdmin(admin.ModelAdmin):
    """Admin interface for managing `Product` models."""
    list_display = ('name', 'category', 'price', 'stock')
    list_filter = ('category',)
    search_fields = ('name', 'description')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)


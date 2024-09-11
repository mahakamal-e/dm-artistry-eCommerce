from django.urls import path
from . import views

urlpatterns = [

    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('count/', views.cart_count, name='cart_count'),  # For logged-in users
    
    path('anon/', views.view_cart_anon, name='view_cart_anon'),  # For anonymous users
    path('anon/add/<int:product_id>/', views.add_to_cart_anon, name='add_to_cart_anon'),
    path('anon/remove/<int:product_id>/', views.remove_from_cart_anon, name='remove_from_cart_anon'),
]
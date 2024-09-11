from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/<int:id>/', views.product_detail, name='product_detail'),
    
    path('', views.home_view, name='home'),
   
    
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/count/', views.cart_count, name='cart_count'),  # For logged-in users
    path('cart/count-unauthenticated/', views.cart_count_unauthenticated, name='cart_count_unauthenticated'),  # For non-logged-in users

]

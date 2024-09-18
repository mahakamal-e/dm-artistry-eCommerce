from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/<int:id>/', views.product_detail, name='product_detail'),
    
    path('', views.home_view, name='home'),
    path('about/', views.about, name='about'),
     path('contact/', views.contact_us, name='contact'),
]

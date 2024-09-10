from django.urls import path
from . import views
from shop.views import  profile


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.my_login, name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', views.custom_logout, name='logout'),
   
]

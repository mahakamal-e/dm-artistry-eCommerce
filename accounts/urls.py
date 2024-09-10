from django.urls import path
from . import views
from shop.views import  profile


urlpatterns = [
    path('register/', views.register, name='register'),

   
]
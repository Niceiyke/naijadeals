
from django.urls import path
from .views import ListProducts

urlpatterns = [
    path('',ListProducts, name='list_products')
]
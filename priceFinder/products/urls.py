
from django.urls import path
from .views import ListProducts

urlpatterns = [
    path('<str:id>',ListProducts, name='list_products')
]
from django.shortcuts import render
from .models import Product

# Create your views here.

def ListProducts (request,id):

    products =Product.objects.filter(category=id)
    context= {
        'products':products
    }

    return render(request,'products/products.html',context)


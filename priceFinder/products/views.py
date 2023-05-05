from django.shortcuts import render
from .models import Product

# Create your views here.

def ListProducts (request):

    products =Product.objects.all()
    print(len(products))

    context= {
        'products':products
    }

    return render(request,'products/products.html',context)


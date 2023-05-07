from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product

# Create your views here.

def ListProducts (request,id):

    qs =Product.objects.filter(category=id)

    paginator = Paginator(qs, 20)  # Show 25 contacts per page.

    page = request.GET.get("page")
    products = paginator.get_page(page)

    context= {
        
        'products':products
        
    }

    return render(request,'products/products.html',context)


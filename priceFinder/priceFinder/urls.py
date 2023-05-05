
from django.contrib import admin
from django.urls import path,include
from .views import Homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/',include('products.urls')),
    path('',Homepage, name='home')
]

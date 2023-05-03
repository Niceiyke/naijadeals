
from django.contrib import admin
from django.urls import path
from .views import Homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Homepage, name='home')
]

from django.http import HttpResponse
from django.shortcuts import render

def Homepage(request):


    return render(request,'pages/home.html',{})

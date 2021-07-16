from django.shortcuts import render
from django.http import HttpResponse

def customers(request):
    return render(request,'accounts/customers.html')

def products(request):
   return render(request,'accounts/products.html')

def dashboard(request):
   return render(request,'accounts/dashboard.html')
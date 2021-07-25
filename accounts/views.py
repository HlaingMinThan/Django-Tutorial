from django.shortcuts import render,redirect
from django.http import HttpResponse
from accounts.models import *
from accounts.forms import *
def customers(request,id):
   customer=Customer.objects.get(id=id)
   orders=customer.order_set.all()
   order_count=orders.count()
   return render(request,'accounts/customers.html',{
      'customer':customer,
      'orders':orders,
      'order_count':order_count
   })

def products(request):
   products=Product.objects.all()
   return render(request,'accounts/products.html',{
      'products':products
   })

def dashboard(request):
   customers=Customer.objects.all()
   orders=Order.objects.all()
   total=orders.count();
   delivered=Order.objects.filter(status="delivered").count()
   pending=Order.objects.filter(status="pending").count()
   return render(request,'accounts/dashboard.html',{
      'customers':customers,
      'orders':orders,
      'total':total,
      'delivered':delivered,
      'pending':pending
   })

def orderCreate(request):
   form=OrderForm()
   if request.method=="POST":
    
      form=OrderForm(request.POST)
      if form.is_valid():
         form.save();
         return redirect('/');
   
   return render(request,'accounts/order_form.html',{
      'form':form
   })

def orderUpdate(request,orderId):
   order=Order.objects.get(id=orderId);
   form=OrderForm(instance=order)
   if request.method=="POST":
    
      form=OrderForm(request.POST,instance=order)
      if form.is_valid():
         form.save();
         return redirect('/');
   
   return render(request,'accounts/order_form.html',{
      'form':form
   })

def orderDelete(request,orderId):
   order=Order.objects.get(id=orderId);
   if request.method=="POST":
      order.delete();
      return redirect('/');
  
   return render(request,'accounts/order_delete.html',{
      'order':order
   })
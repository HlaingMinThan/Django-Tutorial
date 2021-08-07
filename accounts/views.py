from accounts.decorators import authenticated_user
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from accounts import forms
from accounts.models import *
from accounts.forms import *
from .filters import *
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
@login_required(login_url='/login')
def customers(request,id):
   customer=Customer.objects.get(id=id)
   orders=customer.order_set.all()
   order_count=orders.count()
   filterObj=OrderFilter(request.GET,queryset=orders)
   orders=filterObj.qs
   return render(request,'accounts/customers.html',{
      'customer':customer,
      'orders':orders,
      'order_count':order_count,
      'filterObj':filterObj
   })

@login_required(login_url='/login')
def products(request):
   products=Product.objects.all()
   return render(request,'accounts/products.html',{
      'products':products
   })

@login_required(login_url='/login')
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

@login_required(login_url='/login')
def orderCreate(request,customerId):
   OrderFormSet=inlineformset_factory(Customer,Order,fields=('product','status'),extra=10)
   customer=Customer.objects.get(id=customerId);
   formset=OrderFormSet(instance=customer,queryset=Order.objects.none())
   if request.method=="POST":
    
      formset=OrderFormSet(request.POST,instance=customer)
      if formset.is_valid():
         formset.save();
         return redirect('/');
   
   return render(request,'accounts/order_form.html',{
      'formset':formset
   })

@login_required(login_url='/login')
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

@login_required(login_url='/login')
def orderDelete(request,orderId):
   order=Order.objects.get(id=orderId);
   if request.method=="POST":
      order.delete();
      return redirect('/');
  
   return render(request,'accounts/order_delete.html',{
      'order':order
   })

@authenticated_user
def register(request):
   form=RegisterForm()
   if request.method=="POST":
       form=RegisterForm(request.POST)
       if form.is_valid():
          form.save();
          return redirect('/')
   return render(request,'accounts/register.html',{
      'form':form
   });

@authenticated_user
def userLogin(request):
   if request.method=="POST":
      username=request.POST['username']
      password=request.POST['password']

      user=authenticate(request,username=username,password=password)
      if user is not None :
         login(request,user)
         return redirect('/')
      else :
         messages.error(request,'username and password is incorrect')
         return redirect('/login')
   return render(request,'accounts/login.html')

def userLogout(request):
   logout(request)
   return redirect('/login')
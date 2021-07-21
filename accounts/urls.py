from django.contrib import admin
from django.urls import path
from . import views;


urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('customers/<int:id>',views.customers,name='customers.show'),
    path('products/',views.products,name='products'),
]
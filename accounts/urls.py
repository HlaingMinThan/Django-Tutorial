from django.contrib import admin
from django.urls import path
from . import views;


urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('customers/<int:id>',views.customers,name='customers.show'),
    path('customer_profile/',views.customer_profile,name='customers.customer_profile'),
    path('products/',views.products,name='products'),
    path('order/create/<int:customerId>',views.orderCreate,name='order.create'),
    path('order/update/<int:orderId>',views.orderUpdate,name='order.update'),
    path('order/delete/<int:orderId>',views.orderDelete,name='order.delete'),
    path('register/',views.register,name='register'),
    path('login/',views.userLogin,name='login'),
    path('logout/',views.userLogout,name='logout'),
]
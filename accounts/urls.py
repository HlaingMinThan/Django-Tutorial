from django.contrib import admin
from django.urls import path
from . import views;


urlpatterns = [
    path('',views.dashboard),
    path('customers/<int:id>',views.customers),
    path('products/',views.products),
]
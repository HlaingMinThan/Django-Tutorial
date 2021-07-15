from django.contrib import admin
from django.urls import path
from . import views;


urlpatterns = [
    path('',views.dashboard),
    path('about/',views.about),
    path('contact/',views.contact),
]
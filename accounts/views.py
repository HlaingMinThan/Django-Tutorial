from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse('about page')

def contact(request):
    return HttpResponse('contact page')

def dashboard(request):
    return HttpResponse('dashboard page')
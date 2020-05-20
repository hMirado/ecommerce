from django.shortcuts import render
from .models import Products


def home(request):
    products = Products.objects.all()
    template = 'products/home.html'
    context = {'products': products}
    return render(request, template, context)


def all(request):
    products = Products.objects.all()
    context = {"all_products": products}
    template = 'products/all.html'
    return render(request, template, context)

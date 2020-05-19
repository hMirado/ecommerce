from django.shortcuts import render
from .models import Products

def home(request):
    if request.user.is_authenticated:
        username_is = "Mirado using locals"
        #context = locals()
        context = {"username_is": request.user}
    else:
        context = {"username_is": request.user}
    template = 'products/home.html'
    return render(request, template, context)

def all(request):
    products = Products.objects.all()
    context = {"all_products": products}
    template = 'products/all.html'
    return render(request, template, context)
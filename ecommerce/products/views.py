from django.shortcuts import render, Http404
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


def single(request, slug):
    try:
        productSlug = Products.objects.get(slug=slug)
        context = {"productSlug": productSlug}
        template = 'products/single-product.html'
        return render(request, template, context)
    except:
        raise Http404

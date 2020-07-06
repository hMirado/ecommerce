from django.shortcuts import render, Http404, HttpResponse
from .models import Products, ProductImage, Variation
from marketing.models import MarketingMessage


def home(request):
    products = Products.objects.all()
    template = 'products/home.html'
    context = {'products': products}
    return render(request, template, context)


def all(request):
    products = Products.objects.all()
    context = {"products": products}
    template = 'products/all.html'
    return render(request, template, context)


def single(request, slug):
    try:
        productSlug = Products.objects.get(slug=slug)
        # images = Products.productimage_set.all()
        images = ProductImage.objects.filter(product=productSlug)
        context = {"productSlug": productSlug, "images": images}
        template = 'products/single.html'
        return render(request, template, context)
    except:
        raise Http404


def search(request):
    try:
        query = request.GET.get('query')
    except:
        query = None
    if query:
        products = Products.objects.filter(title__icontains=query)
        context = {'request': query, 'products': products}
        template = 'products/results.html'
    else:
        context = {}
        template = 'products/results.html'
    return render(request, template, context)

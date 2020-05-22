from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Cart
from products.models import Products


def view(request):
    cart = Cart.objects.all()[0]
    context = {"cart": cart}
    template = "carts/view.html"
    return render(request, template, context)


def update_cart(request, slug):
    cart = Cart.objects.all()[0]
    try:
        product = Products.objects.get(slug=slug)
    except product.DoesNotExist:
        pass
    except:
        pass
    
    if product not in cart.products.all():
        cart.products.add(product)
    else:
        cart.products.remove(product)

    new_total = 0.00
    for item in cart.products.all():
        new_total += float(item.price)

    cart.total = new_total
    cart.save()

    return HttpResponseRedirect(reverse('carts:my_cart'))

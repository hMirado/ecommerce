from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Cart
from products.models import Products


def view(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id = None

    if the_id:
        cart = Cart.objects.get(id=the_id)
        context = {'cart': cart}
    else:
        empty_message = "Your cart is empty, please kepp shopping"
        context = {"empty": True, "empty_message": empty_message}

    # cart = Cart.objects.all()[0]
    # context = {"cart": cart}
    template = "carts/view.html"
    return render(request, template, context)


def update_cart(request, slug):
    request.session.set_expiry(120000)
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    try:
        cart = Cart.objects.get(id=the_id)
    except Cart.DoesNotExist:
        cart = None

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

    request.session['items_total'] = cart.products.count()
    # print(cart.products.count())
    cart.total = new_total
    cart.save()

    return HttpResponseRedirect(reverse('carts:my_cart'))

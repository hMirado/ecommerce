from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import time, string, random
from .models import Order
from carts.models import Cart
# from orders import utils


def id_generator(length = 10, str = string.ascii_lowercase + string.ascii_uppercase + string.digits):
    the_id =  "".join(random.choice(str) for i in range(length))
    try:
        order = Order.objects.get(order_id=the_id)
        id_generator()
    except Order.DoesNotExist:
        return the_id


# require user login
@login_required
def checkout(request):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except: #Cart.DoesNotExist:
        the_id = None
        return HttpResponseRedirect(reverse("carts:my_cart")) # url (/my_cart/)

    try:
        new_order = Order.objects.get(cart=cart)
    except Order.DoesNotExist:
        new_order = Order()
        new_order.cart = cart
        new_order.user = request.user
        new_order.order_id = id_generator()
        new_order.save()
    except:
        # work on some error message
        return HttpResponseRedirect(reverse("carts:my_cart"))

    # assign address 
    # run credit card
    if new_order.status == "Finished":
        # cart.delete()
        del request.session['cart_id']
        del request.session['items_total']
        return HttpResponseRedirect(reverse("carts:my_cart"))

    context = {}
    template = "products/home.html"
    return render(request, template, context)


def orders(request):
    context = {}
    template = "orders/user.html"
    return render(request, template, context)

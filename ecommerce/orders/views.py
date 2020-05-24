from django.shortcuts import render, HttpResponseRedirect
from  django.urls import reverse
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
def checkout(request):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except: #Cart.DoesNotExist:
        the_id = None
        return HttpResponseRedirect(reverse("carts:my_cart")) # url (/my_cart/)

    new_order, created = Order.objects.get_or_create(cart=cart)
    if created:
        # assign a user to the order
        new_order.order_id = id_generator() # str(time.time())
        new_order.save()

    new_order.user = request.user
    new_order.save()
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

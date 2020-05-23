from django.shortcuts import render, HttpResponseRedirect
from  django.urls import reverse
import time, random
from .models import Order
from carts.models import Cart

def creatde_id():
    caracteres = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789@&é!ççà*$€£ù%?+#-"
    longueur = 20
    id = ""
    compteur = 0

    while compteur < longueur:
        lettre = caracteres[random.randint(0, len(caracteres)-1)]
        id += lettre
        compteur += 1
    print(id)
    return id


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
        new_order.order_id = creatde_id() # str(time.time())
        new_order.save()

    # assign address
    # run credit card
    if new_order.status == "Finished":
        cart.delete()
        del request.session['cart_id']
        del request.session['items_total']
        return HttpResponseRedirect(reverse("carts:my_cart"))

    context = {}
    template = "products/home.html"
    return render(request, template, context)

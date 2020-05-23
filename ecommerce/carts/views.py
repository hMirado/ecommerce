from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Cart, CartItem
from products.models import Products, Variation


def view(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id = None

    if the_id:
        try:
            cart = Cart.objects.get(id=the_id)
            context = {'cart': cart}
        except Cart.DoesNotExist:
            cart = None
    else:
        empty_message = "Your cart is empty, please kepp shopping"
        context = {"empty": True, "empty_message": empty_message}

    template = "carts/view.html"
    return render(request, template, context)


def add_to_cart(request, slug):
    request.session.set_expiry(120000)

    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id)

    try:
        product = Products.objects.get(slug=slug)
    except product.DoesNotExist:
        pass
    except:
        pass

    product_var = []
    if request.method == "POST":
        qty = request.POST['qty']
        for item in request.POST:
            key = item
            val = request.POST[key]
            try:
                v = Variation.objects.get(
                    product=product, category__iexact=key, title__iexact=val)
                product_var.append(v)
            except:
                pass

        cart_item = CartItem.objects.create(cart=cart, product=product)
        if len(product_var) > 0:
            cart_item.variations.add(*product_var)
        cart_item.quantity = qty
        cart_item.save()

        new_total = 0.00
        for item in cart.cartitem_set.all():
            line_total = float(item.product.price) * float(item.quantity)
            new_total += line_total

        request.session['items_total'] = cart.cartitem_set.count()
        cart.total = new_total
        cart.save()
        return HttpResponseRedirect(reverse('carts:my_cart'))

    return HttpResponseRedirect(reverse('carts:my_cart'))

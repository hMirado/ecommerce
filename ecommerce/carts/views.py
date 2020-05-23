from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Cart, CartItem
from products.models import Products


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


def update_cart(request, slug):
    request.session.set_expiry(120000)

    try:
        qty = request.GET.get('qty')
        update_qty = True
    except:
        qty = None
        update_qty = False

    notes = {}
    try:
        color = request.GET.get("color")
        notes['color'] = color
    except:
        color = None
    try:
        size = request.GET.get("size")
        notes['size'] = size
    except:
        size = None

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

    # qty = 12
    cart_item, created = CartItem.objects.get_or_create( cart=cart, product=product)
    if created:
        print('YEAH')
    if update_qty and qty: # if int(qty) = 0
        if int(qty) == 0:
            cart_item.delete()
        else:
            cart_item.quantity = qty
            cart_item.notes = notes
            cart_item.save()
    else:
        pass

    '''
    if cart_item not in cart.items.all():
        # cart.products.add(product)
        cart.items.add(cart_item)
    else:
        # cart.products.remove(product)
        cart.items.remove(cart_item)
    '''

    new_total = 0.00
    for item in cart.cartitem_set.all():
        # print(item.quantity)
        line_total = float(item.product.price) * float(item.quantity)
        new_total += line_total

    request.session['items_total'] = cart.cartitem_set.count()
    cart.total = new_total
    cart.save()

    return HttpResponseRedirect(reverse('carts:my_cart'))

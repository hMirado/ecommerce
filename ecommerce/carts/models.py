from django.db import models
from products.models import Products


class CartItem(models.Model):
    # cart foreign key
    product = models.ForeignKey(Products, blank=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    # line total
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.product.title


class Cart(models.Model):
    items = models.ManyToManyField(CartItem, blank=True)
    products = models.ManyToManyField(Products, blank=True)
    total = models.DecimalField(max_digits=65, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return "Cart id: %s" %(self.id)

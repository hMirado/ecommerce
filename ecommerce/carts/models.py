from django.db import models
from products.models import Products

class Cart(models.Model):
    products = models.ManyToManyField(Products, blank=True)
    total = models.DecimalField(max_digits=65, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    

    def __str__(self):
        return "Cart id: %s" %(self.id)

    # def get_absolute_url(self):
    #     return reverse("Cart_detail", kwargs={"pk": self.pk})

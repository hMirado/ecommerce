from django.db import models
from carts.models import Cart

STATUS_CHOICE = (
    ("Started", "Started"),
    ("Abandoned", "Abandoned"),
    ("Finished", "Finished")
)

class Order(models.Model):
    # add user
    # address
    order_id = models.CharField(max_length=120, default='ABC', unique=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=120, choices=STATUS_CHOICE, default="Started")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.order_id

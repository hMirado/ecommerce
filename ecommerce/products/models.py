from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=120, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=65, default=29.99)
    sale_price = models.DecimalField(decimal_places=2, max_digits=65, null=True, blank=True)
    image = models.FileField(upload_to='products/images/', null=True)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def getPrice(self):
        return self.price
from django.urls import reverse
from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=120, null=False, blank=False,  unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=65, default=29.99)
    sale_price = models.DecimalField(decimal_places=2, max_digits=65, null=True, blank=True)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class meta:
        unique_together = ('title', 'slug')

    def getPrice(self):
        return self.price

    def get_absolute_url(self):
        return reverse("products:single_product", kwargs={"slug": self.slug})
        #return "/products/products/%s/" % (self.slug)
    

    
class ProductImage(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    image = models.FileField(upload_to='products/images/', null=True)
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = " ProductImage"
        verbose_name_plural = "ProductImages"

    def __str__(self):
        return self.product.title


class VariationManager(models.Manager):
    def all(self):
        return super(VariationManager, self).filter(active=True)

    def sizes(self):
        return self.all().filter(category='size')

    def colors(self):
        return self.all().filter(category='color')


VAR_CATEGORIES = (
    ('size', 'size'),
    ('color', 'color'),
    ('package', 'package')
)

class Variation(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    category = models.CharField(max_length=120, choices=VAR_CATEGORIES, default='size')
    title = models.CharField(max_length=120)
    image = models.ForeignKey(ProductImage, null=True, blank=True, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=65, decimal_places=2, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    objects = VariationManager()

    def __str__(self):
        return self.title

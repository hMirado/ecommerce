from django.contrib import admin
from .models import Products, ProductImage, Variation

class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    search_fields = ['title', 'description']
    list_display = ['title', 'description', 'price', 'active', 'updated']
    list_editable = ['price', 'active']
    list_filter = ['price', 'active']
    readonly_fields = ['updated', 'timestamp']
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = Products

admin.site.register(Products, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Variation)

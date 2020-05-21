from django.urls import path, re_path
from products import views

app_name = 'products'

urlpatterns = [
    path('products/', views.all, name='products'),
    path('search/', views.search, name='search'),  # search product
    re_path('products/(?P<slug>[\w-]+)/', views.single, name='single_product'),
    # (?P<all_items>.*)
    # (?p<id>\d+)
] 

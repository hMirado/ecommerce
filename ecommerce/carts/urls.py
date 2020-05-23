from django.urls import path, re_path
from carts import views

app_name = 'carts'

urlpatterns = [
    re_path('carts/(?P<slug>[\w-]+)/', views.add_to_cart, name='add_to_cart'),
    path('carts/', views.view, name='my_cart'),
]

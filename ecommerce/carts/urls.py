from django.urls import path, re_path
from carts import views

app_name = 'carts'

urlpatterns = [
    re_path('carts/(?P<slug>[\w-]+)/', views.update_cart, name='update_cart'),
    path('carts/', views.view, name='my_cart'),
]

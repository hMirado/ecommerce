from django.urls import path, re_path
from carts import views

app_name = 'carts'

urlpatterns = [
    path('cart/', views.view, name='cart'),
]

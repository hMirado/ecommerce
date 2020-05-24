from django.urls import path, re_path
from orders import views

app_name = 'orders'

urlpatterns = [
    path('checkout/', views.checkout, name='my_checkout'),
    path('orders/', views.orders, name='user_order'),
]

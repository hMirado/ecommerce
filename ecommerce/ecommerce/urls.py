from django.contrib import admin
from django.urls import path
from products import views
admin.autodiscover()

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.all, name='products'),
    path('admin/', admin.site.urls),
]

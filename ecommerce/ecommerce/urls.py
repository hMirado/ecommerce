from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from products import views
admin.autodiscover()

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', include('products.urls', namespace='products')),  # products url
    path('carts/', include('carts.urls', namespace='carts')),  # cart url
    path('orders/', include('orders.urls', namespace='orders')),  # checkout url
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),  # accounts url
    path('markeing/', include('marketing.urls', namespace='marketing')), # ajax | marketing message
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

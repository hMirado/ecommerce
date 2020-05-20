from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, re_path
from products import views
admin.autodiscover()

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.all, name='products'),
    re_path('products/(?P<slug>[\w-]+)/', views.single, name='single-product'),
    # (?P<all_items>.*)
    # (?p<id>\d+)
    path('admin/', admin.site.urls),
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

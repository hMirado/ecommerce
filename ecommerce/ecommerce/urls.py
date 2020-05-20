from django.conf import settings # Afaka alana
from django.contrib import admin
from django.conf.urls.static import static  # Afaka alana
from django.urls import path
from products import views
admin.autodiscover()

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.all, name='products'),
    path('admin/', admin.site.urls),
] 

# Afaka alana
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

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
    urlpatterns += static(settings.STATIC_URL, document=settings.STATIC_ROOT)
    urlpatterns += static(settings.STATIC_URL, document=settings.MEDIA_ROOT)

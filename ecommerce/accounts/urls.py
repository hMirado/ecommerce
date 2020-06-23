from django.urls import path, re_path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    re_path('activate/(?P<activation_key>\w+)/', views.activation_view, name='activation_view'),
    path('logout/', views.logout_view, name='auth_logout'),
    path('login/', views.login_view, name='auth_login'),
    path('register/', views.registration_view,name='auth_register'),
]

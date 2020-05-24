from django.urls import path, re_path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('accounts/logout/', views.logout_view, name='auth_logout'),
    path('accounts/login/', views.login_view, name='auth_login'),
]

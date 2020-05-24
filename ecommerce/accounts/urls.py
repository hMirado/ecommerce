from django.urls import path, re_path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('accounts/logout/', views.logout_view, name='auth_logout'),
]

from django.urls import path, re_path
from marketing import views

app_name = 'marketing'

urlpatterns = [
    re_path('update_marketing_message/$', views.dismiss_marketing_message, name='dismiss_marketing_message'),
]

from django.urls import path
from . import views
path('ibilgailuak/main/', views.main_page, name='horri-nagusia'),
path('ibilgailuak/kotxe/list', views.kotxe_list, name='kotxe-zerrenda')
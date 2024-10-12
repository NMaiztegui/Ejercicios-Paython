from django.urls import path
from . import views
urlpatterns = [
path('main/', views.main_page, name='horri-nagusia'),
path('kotxe/list/', views.kotxe_list, name='kotxe-zerrenda'),
path('kotxea/new/', views.kotxe_new, name='kotxea-new'),
path('bezero/', views.bezeroa_list, name='bezeroak-zerrenda'),
path('bezero/new/',views.bezeroa_new, name='bezeroa-new'),
path('alokatuak/', views.alokatuak_list, name='alokatuak-zerrenda'),
path('alokatuak/new', views.alokatuak_new, name='alokatuak-new'),
path ('alokatzea/ezabatu/<int:kod_kotxea>/<int:kod_bezeroa>/', views.alokatzea_ezabatu,name='alokatzea-ezabatu')
]
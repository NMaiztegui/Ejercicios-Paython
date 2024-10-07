from django.urls import path
from . import views
urlpatterns = [
 path('ikasleak/', views.ikasle_list, name='zerrenda-default'),
 path('Ikasle/new/', views.ikasle_new, name='zerrenda-ikasle-new'),
 path('ikasgaiak/', views.ikasgai_list, name='zerrenda-ikasgaiak'),
 path ('ikasgai/new/', views.ikasgai_new, name='zerrenda-ikasgai-new'),
 path('notak/', views.notak_list, name='zerrenda-notak' ),
 path('notak/new/', views.notak_new, name='zerrenda-notak-new' ),
 path('notak/aldatu/<int:kod_ikaslea>/<int:kod_ikasgaia>/', views.nota_aldatu, name='nota-aldatu')

]

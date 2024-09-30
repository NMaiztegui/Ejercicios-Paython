from django.urls import path
from . import views
urlpatterns = [
 path('ikasleak/', views.ikasle_list)
]

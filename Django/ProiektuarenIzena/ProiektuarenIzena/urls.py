"""
URL configuration for ProiektuarenIzena project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Aplikazioa1.urls')) #La función include() se utiliza para incluir otras configuraciones de URLs. En este caso, estás indicando que cualquier solicitud que llegue a la raíz del sitio ('', es decir, /) debe ser manejada por el archivo urls.py #en la aplicación Ariketa1, el archivo urls.py podría definir rutas específicas para manejar diferentes páginas o funciones,
]

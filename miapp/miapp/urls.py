"""miapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

#importar app con mis vistas
from aprendiendoDjango import views

#tambien se puede importar de otras formas
#import miapp.views (pero ahi se deben llamar como miapp.views.index)

urlpatterns = [
    path('admin/', admin.site.urls),
    #se puede reutilizar la misma vista varias veces con distintas url
    path('', views.index , name='inicio'),#al pasar el primer algumento vacio hacemos que sea la ruta principal
    path('pagina/pruebas', views.pagina , name='pagina'), 
    path('hola-mundo/', views.hola_mundo, name='hola_mundo')#paso el nombre  de la ruta y la funcion a ajecutar
]

#aca debo cargar mis vistas 


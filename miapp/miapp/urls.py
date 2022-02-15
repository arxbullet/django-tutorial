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
from django.conf import settings

#importar app con mis vistas
from aprendiendoDjango import views

#tambien se puede importar de otras formas
#import miapp.views (pero ahi se deben llamar como miapp.views.index)

urlpatterns = [
    path('admin/', admin.site.urls),
    #se puede reutilizar la misma vista varias veces con distintas url
    path('', views.index , name='inicio'),#al pasar el primer algumento vacio hacemos que sea la ruta principal
    #redirecciones , ejemplo pafina pruebas
    path('pagina-pruebas', views.pagina , name='pagina'),
    path('pagina-pruebas/<int:redirigir>', views.pagina , name='pagina'),  
    path('pagina-contactos/<str:nombre>', views.contacto , name='contactos'), #pasar parametros con <>
    #para que la ruta de arriba no de errores si llega el parametro, debo configurar una ruta para cada caso
    path('pagina-contactos/', views.contacto , name='contactos'),
    path('crear-articulo', views.crear_articulo, name='nuevo_a'),
    path('articulos', views.articulos, name='all'),
    path('borrar-articulos/<int:id>', views.eliminar_articulo, name='borrar'),
    path('mostrar-articulo', views.mostrar_articulo, name='mostrar_a'),
    path('editar-articulo/<int:id>', views.editar_articulo, name='editar_a'),
    path('save-article', views.save_article, name='save-article'),
    path('create-article', views.create_article, name='create-article'),
    path('create_class_form', views.create_form_article, name='create_class_form'),
    path('holamundo', views.hola_mundo, name='hola_mundo')#paso el nombre  de la ruta y la funcion a ajecutar
]

#aca debo cargar mis vistas 


# config para saber si estoy en modo debug y poder ver imagenes en el 
#admin de django

if settings.DEBUG :
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

#configurar titulo panel

admin.site.site_header = 'MASTER EN PYTHON'

#cambiar subtitulo panel 

admin.site.site_title = 'MASTER EN PYTHON'
admin.site.index_title = 'panel de gestion'


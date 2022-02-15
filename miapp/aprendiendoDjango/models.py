from email.policy import default
from tabnanny import verbose
from django.db import models

# Create your models here.
# pequeñas clases que nos generan objetos para trabajar con las entidades bd
# cada modelo representa una entidad y define los campos de un objeto

#crear modelo

class Article(models.Model): #esto creara la tabla article
    title = models.CharField(max_length=60)
    content = models.TextField()
    #ejecutar cambios (nuevo campo y mas capacidades)
    #luego de eso debo ejecutar nuevamente py manage makemigrations y los 2 comandos siguientes
    image = models.ImageField(default='null')
    public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    #la clase meta sirve para asignarle nombres singulares, plugares y orden a nuestras tablas
    class Meta:
        verbose_name ='Articulo'
        verbose_name_plural = 'Articulos'
        ordering = ['id']


class Category(models.Model): 
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name ='categoria'
        verbose_name_plural = 'categorias'

#cada que haga un cambio en mi estructura sql necesito hacer una migración
# esto se hace con el comando python manage.py makemigrations
# luego hay que crear el sql que se ejecutara realmente com el siguiente comando:
# python manage.py sqlmigrate nombredeapp numerodemigracion
# luego para ejecutar este codigo sql debo ir a la consola y escribir :
# python manage.py migrate
# para comprobar que se ejecuto esto en sqlite puedo descargar sqlitebrowser 
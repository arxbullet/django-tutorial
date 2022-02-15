from email.policy import default
from tabnanny import verbose
from django.db import models

# Create your models here.
# pequeñas clases que nos generan objetos para trabajar con las entidades bd
# cada modelo representa una entidad y define los campos de un objeto

#crear modelo

class Article(models.Model): #esto creara la tabla article
    #para modificar los nombres de los campos uso verbose name
    title = models.CharField(max_length=60, verbose_name='titulo')
    content = models.TextField(verbose_name='contenido')
    #ejecutar cambios (nuevo campo y mas capacidades)
    #luego de eso debo ejecutar nuevamente py manage makemigrations y los 2 comandos siguientes
    image = models.ImageField(default='null',verbose_name='imagen')
    public = models.BooleanField(verbose_name='publico')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='creado el ')
    updated_at = models.DateTimeField(auto_now_add=True,verbose_name='actualizado el ')

    #la clase meta sirve para asignarle nombres singulares, plugares y orden a nuestras tablas
    class Meta:
        verbose_name ='Articulo'
        verbose_name_plural = 'Articulos'
        ordering = ['id']

    #metodos magicos , este nos imprime los objetos con otro nombre en el panel de administracion
    def __str__(self):
        return f'{self.title} creado el {self.created_at}'

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
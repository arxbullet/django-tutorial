from django.db import models

# Create your models here.
# pequeñas clases que nos generan objetos para trabajar con las entidades bd
# cada modelo representa una entidad y define los campos de un objeto

#crear modelo

class Article(models.Model): #esto creara la tabla article
    title = models.CharField(max_length=50)
    content = models.TextField()
    public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model): 
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


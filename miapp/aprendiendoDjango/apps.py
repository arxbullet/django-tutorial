from tabnanny import verbose
from django.apps import AppConfig


class AprendiendodjangoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aprendiendoDjango'
    verbose_name = 'aplicacionMasterPython' #esto sirve para cambiar el nombre de la app en el panel de administrador, 
    #luego de eso, hay que cambiar el nombre en settings sumando .apps.nombredeestaclase.

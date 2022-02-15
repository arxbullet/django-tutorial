from django.contrib import admin
from .models import *

# Register your models here.

#esta clase nos permite mostrar campos de solo lectura
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields= ('created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

#configurar titulo panel

admin.site.site_header = 'MASTER EN PYTHON'

#cambiar subtitulo panel 

admin.site.site_title = 'MASTER EN PYTHON'
admin.site.index_title = 'panel de gestion'

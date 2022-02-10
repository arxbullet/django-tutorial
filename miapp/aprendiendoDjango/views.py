from django.shortcuts import render, HttpResponse

# Create your views here.

#mvc = modelo vista controlador
#mvt = modelo vista templates


def index(request):#inicio
    return HttpResponse("""
    <h1>inicio</h1>
    """)

def pagina(request):
    return HttpResponse("""
    <h1>pagina de mi web</h1>
    """)

def hola_mundo(request):
    #return HttpResponse('holamundo con django') esto es una respuesta http
    return HttpResponse("""<h1>holamundo con django</h1>""") #tambien puedo devolver html


#para que este metodo funcione debo cargarlo en una url en urls.py


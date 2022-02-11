from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

#mvc = modelo vista controlador
#mvt = modelo vista templates

#para indexar y enlazar mis vistas, puedo enlazar un menu dentro de la misma 
#funcion, o puedo hacer un layout que se cargue en cada vista
layout = """
    <h1>
    sitio web con django
    </h1>
    <ul>
    <li> <a href = '/'> inicio </a> </li>
    <li> <a href = '/holamundo'> hola mundo </a> </li>
    <li> <a href = '/pagina-pruebas'> pagina pruebas </a> </li>
    <li> <a href = '/pagina-contactos'> pagina contactos </a> </li>
    </ul>

"""


def index(request):#inicio
    #tambien puedo devolver un html en una variable
    html = """
    <h1>inicio</h1>
    <p> años hasta el 2050: </p>
    <ul>
    """
    
    #tambien puedo usar todo tipo de logicas de python

    year = 2021
    while year <= 2050 :
        html += f'<li>{str(year)}</li>'
        year += 1
    
    html += '</ul>'

    #concatenare el layout al html 
    return HttpResponse(layout+ html)
    '''return HttpResponse("""
    <h1>inicio</h1>
    """)'''

def pagina(request, redirigir = 0):
    if redirigir == 1 :
        return redirect('/')
        #tambien puedo pasarle un nombre de ruta y sus parametros
        #return redirect('inicio', nombre = 'vale')
    return HttpResponse(layout+"""
    <h1>pagina de mi web</h1>
    """)

# pasar parametros por las rutas
def contacto(request, nombre='valentina'):#para que este codigo no de error si no llegan los 
    #parametros, podemos darle valor por defecto a los parametros
    return HttpResponse(layout+f"""
    <h1>pagina contactos</h1>
    <h2>{nombre}</h2>
    """)
    #puedo tener cuantos parametros necesite.

def hola_mundo(request):
    #return HttpResponse('holamundo con django') esto es una respuesta http
    return HttpResponse(layout+"""<h1>holamundo con django</h1>""") #tambien puedo devolver html


#para que este metodo funcione debo cargarlo en una url en urls.py



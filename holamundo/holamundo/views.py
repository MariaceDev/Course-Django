#las vistas siempre van a tener un parámetro que es el request, la petición de ejecutar esta vista
#En este ejemplo nos saltamos los modelos y las plantillas con las que trabajaremos más adelente

from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola mundo")

# Ya tenemos la vista creada, ahora necesitamos asociar una ruta que ejecute la vista. 
# Para ello nos vamos el urls.py y la definimos: 

def despedida (request):
    return HttpResponse("Adiós, hasta otra")

def adulto (request, edad):
    if(edad >= 18):
        return HttpResponse ("Es mayor de edad.")
    else:
        return HttpResponse ("No eres mayor de edad.")
    
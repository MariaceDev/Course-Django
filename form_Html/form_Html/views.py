from django.shortcuts import render
from django.http import HttpResponse

def getForm(request):
    return render(request, 'form.html', {})

def getGoal(request):

    if request.method != 'GET':
        return HttpResponse("El método POST no está soportado para esta ruta")
    
    name = request.GET['name']
    return render(request, 'success.html', {'name': name})

def postForm(request):
     return render(request, 'postForm.html', {})

def postGoal(request):

    if request.method != 'POST':
        return HttpResponse("El método GET no está soportado para esta ruta")

    info = request.POST['info']
    return render(request, 'postSuccess.html', {'info': info})



        

from django.http import HttpResponse
from django.shortcuts import render
from .forms import CommentForm, ContactForm

def form(request):
    comment_form = CommentForm({'name': 'Mari', 'url': 'https:// www.mariacedev.com', 'comment': 'Hola amigos'})
    return render(request, 'form.html', {'comment_form': comment_form})

'''''def goal(request):
    if request.method != 'GET':
        return HttpResponse('Método no permitido')
    
    return HttpResponse(request.GET['name']) '''''

def goal(request):
    if request.method != 'POST':
        return HttpResponse('Método no permitido')
    
    return HttpResponse(request.POST['name'])

def widget(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'widget.html', {'form': form})
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #Todas las acciones cuando los datos son correctos
            return HttpResponse("Válido")
        else:
            #Comunicamos al usuario que los datos no son válidos
            return render(request, 'widget.html', {'form': form})


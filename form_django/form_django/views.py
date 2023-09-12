from django.http import HttpResponse
from django.shortcuts import render
from .forms import CommentForm

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


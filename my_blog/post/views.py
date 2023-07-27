from django.shortcuts import render
from .models import Author, Entry

def queries (request):
    # Obtener todos los elementos
    authors = Author.objects.all()

    # Obtener datos filtrados por condición
    filtered = Author.objects.filter(email='aprilcontreras@example.org')

    # Obtener un único objeto (filtrado)
    author = Author.objects.get(id=1)

    # Obtener los 10 primeros elementos
    limits = Author.objects.all()[:10]

    # Obtener 10 elemetos saltando los 5 primeros
    offsets = Author.objects.all()[5:10] 
  
    return render(request, 'post/queries.html', {'authors': authors, 'filtered': filtered, 'author': author, 'limits': limits, 'offsets':  offsets})
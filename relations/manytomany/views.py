from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Publication

def create (request):
     
    pub1 = Publication.objects.get(id=1)
    result = pub1.article_set.all()


    return HttpResponse(pub1)
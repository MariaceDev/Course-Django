from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date

def create(request):
    rep = Reporter(first_name='Mina', last_name='Repiso', email='mina@demo.com')
    rep.save()

    art1 = Article(headline='Los modelos de lenguaje', pub_date = date(2023,1,8), reporter=rep)
    art1.save()
    art2 = Article(headline='Machine learning', pub_date = date(2023,2,8), reporter=rep)
    art2.save()
    art3 = Article(headline='Frame para metáforas ontológicas', pub_date = date(2023,3,8), reporter=rep)
    art3.save()

    result = art1.reporter.first_name
    result1 = rep.article_set.all() #nombre del article y set, después todo igual que en las consultas
    result2 = rep.article_set.filter(headline='Los modelos de lenguaje')
    result3 = rep.article_set.count()
    
    return HttpResponse(result3)

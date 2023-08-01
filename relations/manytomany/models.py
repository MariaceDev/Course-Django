from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title
    


class Article(models.Model): #Como trabajamos en aplicaciones autocontenidas, no nos va a dar ningún problema que ya tengamos una clase Article en otra aplicación
    headline = models.CharField(max_length=100)
    publicacions = models.ManyToManyField(Publication) #Para definir el many to many, no hace falta el delete porque e crea una tabla a parte
    
    def __str__(self):
        return self.headline
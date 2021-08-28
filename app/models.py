from __future__ import unicode_literals
from django.db import models


# Create your models here.
#    
class ShowManager(models.Manager):

    def validador(self, postData):
        errors = {}
        # agregue claves y valores al diccionario de errores para cada campo no válido
        if len(postData['title']) < 3:
            errors["title"] = "Falta ingresar correctamente la información al campo title"
        if len(postData['network']) < 3:
            errors["network"] = "Falta ingresar correctamente la información al campo network"
        if len(postData['release']) < 3:
            errors["release"] = "Falta ingresar correctamente la información al campo release"
        if len(postData['description']) < 3:
            errors["release"] = "Falta ingresar correctamente la información al campo description"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=200)
    network = models.CharField(max_length=80)
    release_date = models.DateField()
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __str__(self):
        return f"{self.title} ({self.network})"

    def __repr__(self):
        return f"{self.title} ({self.network})"
from django.db import models
from Direcciones.models import Domicilio

# Create your models here.
class Equipo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.modelo

class Sector(models.Model):
    descripcion = models.CharField(max_length=200)
    ubicacion = models.ForeignKey(Domicilio, on_delete=models.CASCADE, related_name='sector_domicilio')

    def __str__(self):
        return self.descripcion
from django.db import models

# Create your models here.

class Localidad(models.Model):
    nombre = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Domicilio(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE, related_name='domicilio_localidad')

    def __str__(self):
        return self.calle + " #" + self.numero
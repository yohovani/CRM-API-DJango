from django.db import models
from django.urls import reverse
from Direcciones.models import Domicilio
from Equipo.models import Equipo, Sector

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100, blank=True)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=100)
    instalador = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='usuario_empleado')
    domicilio = models.ForeignKey(Domicilio, on_delete=models.CASCADE, related_name='usuario_domicio')
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='usuario_equipo')
    def __str__(self):
        return self.nombre
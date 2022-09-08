from django.db import models
from django.urls import reverse
from Empleados.models import Empleado


# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=100)
    instalador = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='empleado_usuario')

    def __str__(self):
        return self.nombre
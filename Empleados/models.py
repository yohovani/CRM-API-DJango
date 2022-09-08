from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100, blank=True)


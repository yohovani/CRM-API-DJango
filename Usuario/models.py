from django.db import models
from datetime import date
from django.urls import reverse
# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
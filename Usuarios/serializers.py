from rest_framework import serializers

import Usuarios.models
from Usuarios.models import Empleado
from Direcciones.models import Domicilio
from Equipo.models import Equipo


class UsuarioSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    allow_null = True
    many = True
    class Meta:
        model = Usuarios.models.Cliente
        fields = ['id', 'nombre', 'apellido_paterno', 'apellido_materno', 'telefono', 'domicilio', 'instalador', 'equipo']
        depth = 1

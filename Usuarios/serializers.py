from rest_framework import serializers
import Usuarios

class UsuarioSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(max_length=100)
    apellido_paterno = serializers.CharField(max_length=100)
    apellido_materno = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Usuarios.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.apellido_paterno = validated_data.get('apellido_paterno', instance.nombre)
        instance.apellido_materno = validated_data.get('apellido_materno', instance.nombre)

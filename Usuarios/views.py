from django.shortcuts import render
from django.http import  JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from Usuarios.models import Cliente
from Usuarios.serializers import UsuarioSerializer
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET'])
def Usuario_list(request):
    """
        List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

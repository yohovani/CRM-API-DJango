from django.shortcuts import render
from django.http import  JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from Usuarios.models import Cliente
from Usuarios.serializers import UsuarioSerializer
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET', 'POST'])
def Clients_list(request):
    cliente = Cliente.objects.all()
    serializer = UsuarioSerializer(cliente, many=True)
    return JsonResponse(serializer.data, safe=False)

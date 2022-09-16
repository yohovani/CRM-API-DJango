from django.urls import path
from . import views

urlpatterns = [
    path('clientes/all', views.Clients_list, name="clientes_list"),
    path('clientes/cliente/<int:id_cliente>/', views.get_cliente, name="cliente"),
]

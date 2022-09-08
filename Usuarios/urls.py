from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.Usuario_list, name="usuario_list"),
]

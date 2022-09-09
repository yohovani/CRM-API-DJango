from django.contrib import admin
from .models import Domicilio, Localidad

# Register your models here.
admin.site.register(Domicilio)
admin.site.register(Localidad)
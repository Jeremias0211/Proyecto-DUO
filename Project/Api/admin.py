from django.contrib import admin

# ---> Importamos los Modelos (Tablas)
from .models import *

# --> Registramos la Tabla en el sector de Admin
admin.site.register(Producto)
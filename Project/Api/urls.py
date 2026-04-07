from django.urls import path
# --> Importamos las Vistas
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('Productos/', Productos, name='Productos'),
    path('NuevoProducto/', NuevoProductos, name='nuevo_producto'),
    path('ModificarProducto/<Codigo>', ModificarProductos, name='Modificar'),
]

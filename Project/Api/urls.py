from django.urls import path
from django.views.generic import RedirectView

from .views import (
    Catalogo,
    EliminarProducto,
    Home,
    ModificarProductos,
    NuevoProductos,
    PanelVendedor,
)

urlpatterns = [
    path('', Home, name='home'),
    path(
        'productos/',
        RedirectView.as_view(pattern_name='catalogo', query_string=True),
        name='productos_redirect',
    ),
    path('catalogo/', Catalogo, name='catalogo'),
    path('vendedor/productos/', PanelVendedor, name='panel_vendedor'),
    path('productos/nuevo/', NuevoProductos, name='nuevo_producto'),
    path('productos/<int:codigo>/editar/', ModificarProductos, name='Modificar'),
    path('productos/<int:codigo>/eliminar/', EliminarProducto, name='eliminar_producto'),
]

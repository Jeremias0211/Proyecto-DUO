from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import FormularioProductos
from .models import Producto


def _productos_filtrados(request):
    productos = Producto.objects.all().order_by('-Fecha', 'Nombre')
    busqueda = request.GET.get('q', '').strip()
    if busqueda:
        productos = productos.filter(
            Q(Nombre__icontains=busqueda)
            | Q(Descripcion__icontains=busqueda)
            | Q(Categoria__icontains=busqueda)
        )
    return productos, busqueda


def Home(request):
    return render(request, 'Pages/Inicio.html')


def Catalogo(request):
    """Catálogo público para compradores."""
    productos, busqueda = _productos_filtrados(request)
    return render(
        request,
        'Pages/CatalogoProductos.html',
        {'productos': productos, 'busqueda': busqueda},
    )


def PanelVendedor(request):
    """Gestión de productos: alta, edición y baja."""
    productos, busqueda = _productos_filtrados(request)
    return render(
        request,
        'Pages/VerProductos.html',
        {'productos': productos, 'busqueda': busqueda},
    )


def NuevoProductos(request):
    if request.method == 'POST':
        formulario = FormularioProductos(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Producto guardado correctamente.')
            return redirect('panel_vendedor')
        messages.error(request, 'No se pudo guardar. Revisá los datos del formulario.')
    else:
        formulario = FormularioProductos()
    return render(request, 'Pages/NuevoProducto.html', {'formulario': formulario})


def ModificarProductos(request, codigo):
    producto = get_object_or_404(Producto, Codigo=codigo)
    if request.method == 'POST':
        formulario = FormularioProductos(
            data=request.POST,
            files=request.FILES,
            instance=producto,
        )
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Producto actualizado correctamente.')
            return redirect('panel_vendedor')
        messages.error(request, 'No se pudo actualizar. Revisá los datos del formulario.')
    else:
        formulario = FormularioProductos(instance=producto)
    return render(
        request,
        'Pages/ModificarProducto.html',
        {'formulario': formulario, 'producto': producto},
    )


def EliminarProducto(request, codigo):
    if request.method != 'POST':
        messages.error(request, 'No se puede eliminar de esa forma.')
        return redirect('panel_vendedor')
    producto = get_object_or_404(Producto, Codigo=codigo)
    nombre = producto.Nombre
    if producto.Imagen:
        producto.Imagen.delete(save=False)
    producto.delete()
    messages.success(request, f'«{nombre}» fue eliminado del catálogo.')
    return redirect('panel_vendedor')

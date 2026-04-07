from django.shortcuts import render, get_object_or_404
from .forms import *
# Create your views here.


def Home(request):
    return render(request, 'Base.html')

def Productos(request):
    query=Producto.objects.all()
    data={
        'ListarProductos':query
    }
    return render(request, 'Pages/VerProductos.html',data)


def NuevoProductos(request):
    data={
        'Formulario': FormularioProductos()
    }
    if request.method == 'POST':
        formulario = FormularioProductos(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['Mensaje'] = "Producto Guardado Correctamente"
        else:
            data['Mensaje'] = "Error al Guardar el Producto"
    return render(request, 'Pages/NuevoProducto.html', data)



def ModificarProductos(request,Codigo):
    buscar=get_object_or_404(Producto, Codigo=Codigo)
    data={
        'Formulario': FormularioProductos(instance=buscar)
    }
    if request.method == 'POST':
        formulario = FormularioProductos(data=request.POST,instance=buscar,files=request.FILES)
        
        if formulario.is_valid():
            formulario.save()
            data['Mensaje'] = "Producto Modificados Correctamente"
        else:
            data['Mensaje'] = "Error al Actualizar el Producto"
    return render(request, 'Pages/ModificarProducto.html', data)



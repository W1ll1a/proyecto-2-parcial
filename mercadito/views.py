from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Empleados, Cliente,Producto,Proveedores,Facturas
from .forms import EmpleadoForm
from mercadito.forms import EmpleadoForm
from django.urls import reverse_lazy
# Create your views here.


#def expediente_index(request):
#   return HttpResponse("Cargando vistas")

def cliente_index(request):
    return render(request, 'cliente/index.html')

def empleado_index(request):
    if request.method =='POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EmpleadoForm()

    return render(request, 'empleado/formEmpleado.html',{'form':form})

def proveedores_index(request):
    return render(request, 'proveedores/index.html')

def factura_index(request):
    return render(request, 'factura/index.html')

def producto_index(request):
    return render(request, 'producto/index.html')


class Home(generic.TemplateView):
    template_name = 'base/base.html'

class EmpleadoAgregar(generic.CreateView):
    model = Empleados
    form_class = EmpleadoForm
    template_name = 'empleado/formEmpleado.html' 
    success_url = reverse_lazy('Empleado_listar')
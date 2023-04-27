from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Empleados, Cliente,Producto,Proveedores,Facturas
from .forms import EmpleadoForm
from mercadito.forms import*
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.


#def expediente_index(request):
#   return HttpResponse("Cargando vistas")

class EmpleadoCrear(CreateView):
    model = Empleados
    form_class = EmpleadoForm
    template_name = 'empleado/formEmpleado.html' 
    success_url = reverse_lazy('empleado_listar')

class empleado_edit(UpdateView):
    model = Empleados
    form_class = EmpleadoForm
    template_name = 'empleado/formEmpleado.html' 
    success_url = reverse_lazy('empleado_listar')

class empleado_listar(ListView):
    model= Empleados
    template_name='empleado/empleado_listado.html'


class empleado_eliminar(DeleteView):
    model=Empleados
    template_name='empleado/formEmpleado.html'
    success_url =reverse_lazy('empleado_listar')
#proveedores

class proveedoresCrear(CreateView):
    model=Proveedores
    form_class=ProveedorForm
    template_name='Proveedor/formProveedor.html'
    success_url =reverse_lazy('proveedores_listar')

class proveedores_listar(ListView):
    model= Proveedores
    template_name='Proveedor/proveedores_listado.html'


class proveedores_edit(UpdateView):
    model = Proveedores
    form_class = ProveedorForm
    template_name = 'Proveedor/formProveedor.html' 
    success_url = reverse_lazy('proveedores_listar')

class proveedores_eliminar(DeleteView):
    model=Proveedores
    template_name='Proveedor/formProveedor.html'
    success_url =reverse_lazy('proveedores_listar')

#productos

class ProductoCrear(CreateView):
    model=Producto
    form_class=ProductoForm
    template_name='Producto/formProducto.html'
    success_url =reverse_lazy('Producto_listar')

class Producto_listar(ListView):
    model= Producto
    template_name='Producto/producto_listado.html'

class Producto_edit(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Producto/formProducto.html' 
    success_url = reverse_lazy('Producto_listar')

class Producto_eliminar(DeleteView):
    model=Producto
    template_name='Producto/formProducto.html'
    success_url =reverse_lazy('Producto_listar')

#cliente

class clienteCrear(CreateView):
    model=Cliente
    form_class=clienteForm
    template_name='cliente/formCliente.html'
    success_url =reverse_lazy('cliente_listar')

class cliente_listar(ListView):
    model= Cliente
    template_name='cliente/cliente_listado.html'

class cliente_edit(UpdateView):
    model = Cliente
    form_class = clienteForm
    template_name = 'cliente/formCliente.html' 
    success_url = reverse_lazy('cliente_listar')

class cliente_eliminar(DeleteView):
    model=Cliente
    template_name='cliente/formCliente.html'
    success_url =reverse_lazy('cliente_listar')

#factura

class facturaCrear(CreateView):
    model=Facturas
    form_class=facturaForm
    template_name='Facturas/formFactura.html'
    success_url =reverse_lazy('factura_listar')

class factura_listar(ListView):
    model= Facturas
    template_name='Facturas/factura_listado.html'

class factura_edit(UpdateView):
    model = Facturas
    form_class = facturaForm
    template_name = 'Facturas/formFactura.html' 
    success_url = reverse_lazy('factura_listar')

class factura_eliminar(DeleteView):
    model=Facturas
    template_name='Facturas/formFactura.html'
    success_url =reverse_lazy('factura_listar')
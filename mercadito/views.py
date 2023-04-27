from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Empleados, Cliente,Producto,Proveedores,Facturas
from .forms import EmpleadoForm
from mercadito.forms import*
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


#def expediente_index(request):
#   return HttpResponse("Cargando vistas")
class EmpleadoCrear(LoginRequiredMixin,generic.CreateView):
    model = Empleados
    form_class = EmpleadoForm
    template_name = 'empleado/formEmpleado.html' 
    success_url = reverse_lazy('empleado_listar')
    login_url = '/login'

class empleado_edit(LoginRequiredMixin,generic.UpdateView):
    model = Empleados
    form_class = EmpleadoForm
    template_name = 'empleado/formEmpleado.html' 
    success_url = reverse_lazy('empleado_listar')
    login_url = '/login'

class empleado_listar(LoginRequiredMixin,generic.ListView):
    model= Empleados
    template_name='empleado/empleado_listado.html'
    login_url = '/login'


class empleado_eliminar(LoginRequiredMixin,generic.DeleteView):
    model=Empleados
    template_name='empleado/eliminar.html'
    success_url =reverse_lazy('empleado_listar')
    login_url = '/login'
#proveedores

class proveedoresCrear(LoginRequiredMixin,generic.CreateView):
    model=Proveedores
    form_class=ProveedorForm
    template_name='Proveedor/formProveedor.html'
    success_url =reverse_lazy('proveedores_listar')
    login_url = '/login'

class proveedores_listar(LoginRequiredMixin,generic.ListView):
    model= Proveedores
    template_name='Proveedor/proveedores_listado.html'
    login_url = '/login'


class proveedores_edit(LoginRequiredMixin,generic.UpdateView):
    model = Proveedores
    form_class = ProveedorForm
    template_name = 'Proveedor/formProveedor.html' 
    success_url = reverse_lazy('proveedores_listar')
    login_url = '/login'

class proveedores_eliminar(LoginRequiredMixin,generic.DeleteView):
    model=Proveedores
    template_name='Proveedor/eliminar.html'
    success_url =reverse_lazy('proveedores_listar')
    login_url = '/login'

#productos

class ProductoCrear(LoginRequiredMixin,generic.CreateView):
    model=Producto
    form_class=ProductoForm
    template_name='Producto/formProducto.html'
    success_url =reverse_lazy('Producto_listar')
    login_url = '/login'

class Producto_listar(LoginRequiredMixin,generic.ListView):
    model= Producto
    template_name='Producto/producto_listado.html'
    login_url = '/login'

class Producto_edit(LoginRequiredMixin,generic.UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Producto/formProducto.html' 
    success_url = reverse_lazy('Producto_listar')
    login_url = '/login'

class Producto_eliminar(LoginRequiredMixin,generic.DeleteView):
    model=Producto
    template_name='Producto/eliminar.html'
    success_url =reverse_lazy('Producto_listar')
    login_url = '/login'
#cliente

class clienteCrear(LoginRequiredMixin,generic.CreateView):
    model=Cliente
    form_class=clienteForm
    template_name='cliente/formCliente.html'
    success_url =reverse_lazy('cliente_listar')
    login_url = '/login'

class cliente_listar(LoginRequiredMixin,generic.ListView):
    model= Cliente
    template_name='cliente/cliente_listado.html'
    login_url = '/login'

class cliente_edit(LoginRequiredMixin,generic.UpdateView):
    model = Cliente
    form_class = clienteForm
    template_name = 'cliente/formCliente.html' 
    success_url = reverse_lazy('cliente_listar')
    login_url = '/login'

class cliente_eliminar(LoginRequiredMixin,generic.DeleteView):
    model=Cliente
    template_name='cliente/eliminar.html'
    success_url =reverse_lazy('cliente_listar')
    login_url = '/login'
#factura

class facturaCrear(LoginRequiredMixin,generic.CreateView):
    model=Facturas
    form_class=facturaForm
    template_name='Facturas/formFactura.html'
    success_url =reverse_lazy('factura_listar')
    login_url = '/login'
class factura_listar(LoginRequiredMixin,generic.ListView):
    model= Facturas
    template_name='Facturas/factura_listado.html'
    login_url = '/login'

class factura_edit(LoginRequiredMixin,generic.UpdateView):
    model = Facturas
    form_class = facturaForm
    template_name = 'Facturas/formFactura.html' 
    success_url = reverse_lazy('factura_listar')
    login_url = '/login'

class factura_eliminar(LoginRequiredMixin,generic.DeleteView):
    model=Facturas
    template_name='Facturas/formFactura.html'
    success_url =reverse_lazy('factura_listar')
    login_url = '/login'
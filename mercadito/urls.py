from django.urls import path
from . import views
from mercadito.views import Home
from mercadito.views import *

urlpatterns = [
    #path('', views.expediente_index, name='index'),
    #para Empleados
    path('',Home.as_view(), name='Home'),
    path('mercadito/empleado/crear',views.EmpleadoCrear.as_view(), name='empleado_crear'),
    path('mercadito/empleado',views.empleado_listar.as_view(), name='empleado_listar'),
    path('mercadito/empleado/editar/<int:pk>/',views.empleado_edit.as_view(), name='empleado_edit'),
    path('mercadito/empleado/eliminar/<int:pk>/',views.empleado_eliminar.as_view(), name='empleado_eliminar'),
    #Para Proveedores
    path('mercadito/proveedores/crear',views.proveedoresCrear.as_view(), name='proveedores_crear'),
    path('mercadito/proveedores',views.proveedores_listar.as_view(), name='proveedores_listar'),
    path('mercadito/proveedores/editar/<int:pk>/',views.proveedores_edit.as_view(), name='proveedores_edit'),
    path('mercadito/proveedores/eliminar/<int:pk>/',views.proveedores_eliminar.as_view(), name='proveedores_eliminar'),
    #Para Productos
    path('mercadito/producto/crear',views.ProductoCrear.as_view(), name='Producto_crear'),
    path('mercadito/producto',views.Producto_listar.as_view(), name='Producto_listar'),
    path('mercadito/producto/editar/<int:pk>/',views.Producto_edit.as_view(), name='Producto_edit'),
    path('mercadito/producto/eliminar/<int:pk>/',views.Producto_eliminar.as_view(), name='Producto_eliminar'),
    #Para cliente
    path('mercadito/cliente/crear',views.clienteCrear.as_view(), name='cliente_crear'),
    path('mercadito/cliente',views.cliente_listar.as_view(), name='cliente_listar'),
    path('mercadito/cliente/editar/<int:pk>/',views.cliente_edit.as_view(), name='cliente_edit'),
    path('mercadito/cliente/eliminar/<int:pk>/',views.cliente_eliminar.as_view(), name='cliente_eliminar'),
      #Para factura
    path('mercadito/factura/crear',views.facturaCrear.as_view(), name='factura_crear'),
    path('mercadito/factura',views.factura_listar.as_view(), name='factura_listar'),
    path('mercadito/factura/editar/<int:pk>/',views.factura_edit.as_view(), name='factura_edit'),
    path('mercadito/factura/eliminar/<int:pk>/',views.factura_eliminar.as_view(), name='factura_eliminar'),
]

from django.urls import path
from .views import *

urlpatterns = [
    #path('', views.expediente_index, name='index'),
    #para Empleados
    path('mercadito/empleado/crear',EmpleadoCrear.as_view(), name='empleado_crear'),
    path('mercadito/empleado',empleado_listar.as_view(), name='empleado_listar'),
    path('mercadito/empleado/editar/<int:pk>/',empleado_edit.as_view(), name='empleado_edit'),
    path('mercadito/empleado/eliminar/<int:pk>/',empleado_eliminar.as_view(), name='empleado_eliminar'),
    #Para Proveedores
    path('mercadito/proveedores/crear',proveedoresCrear.as_view(), name='proveedores_crear'),
    path('mercadito/proveedores',proveedores_listar.as_view(), name='proveedores_listar'),
    path('mercadito/proveedores/editar/<int:pk>/',proveedores_edit.as_view(), name='proveedores_edit'),
    path('mercadito/proveedores/eliminar/<int:pk>/',proveedores_eliminar.as_view(), name='proveedores_eliminar'),
    #Para Productos
    path('mercadito/producto/crear',ProductoCrear.as_view(), name='Producto_crear'),
    path('mercadito/producto',Producto_listar.as_view(), name='Producto_listar'),
    path('mercadito/producto/editar/<int:pk>/',Producto_edit.as_view(), name='Producto_edit'),
    path('mercadito/producto/eliminar/<int:pk>/',Producto_eliminar.as_view(), name='Producto_eliminar'),
    #Para cliente
    path('mercadito/cliente/crear',clienteCrear.as_view(), name='cliente_crear'),
    path('mercadito/cliente',cliente_listar.as_view(), name='cliente_listar'),
    path('mercadito/cliente/editar/<int:pk>/',cliente_edit.as_view(), name='cliente_edit'),
    path('mercadito/cliente/eliminar/<int:pk>/',cliente_eliminar.as_view(), name='cliente_eliminar'),
      #Para factura
    path('mercadito/factura/crear',facturaCrear.as_view(), name='factura_crear'),
    path('mercadito/factura',factura_listar.as_view(), name='factura_listar'),
    path('mercadito/factura/editar/<int:pk>/',factura_edit.as_view(), name='factura_edit'),
    path('mercadito/factura/eliminar/<int:pk>/',factura_eliminar.as_view(), name='factura_eliminar'),
]

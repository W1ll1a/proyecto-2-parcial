from django.urls import path
from . import views
from mercadito.views import Home


urlpatterns = [
    #path('', views.expediente_index, name='index'),
    path('',Home.as_view(), name='Home'),
    path('mercadito/producto/index',views.producto_index, name='producto_index'),
    path('mercadito/cliente/index',views.cliente_index, name='cliente_index'),
    path('mercadito/factura/index',views.factura_index, name='factura_index'),
    path('mercadito/empleado/index',views.empleado_index, name='empleado_index'),
    path('mercadito/proveedores/index',views.proveedores_index, name='proveedores_index'),
]

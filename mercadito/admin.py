from django.contrib import admin
from mercadito.models import Empleados,Cliente,Proveedores,Facturas,Producto
# Register your models here.
admin.site.register(Empleados)
admin.site.register(Cliente)
admin.site.register(Proveedores)
admin.site.register(Facturas)
admin.site.register(Producto)

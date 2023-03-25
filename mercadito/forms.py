from django import forms
from .models import *

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = ['idEmpleado', 'EmpleadoNombre','EmpleadoEdad']
        labels = {'idEmpleado':"codigo de empleado:",
                  'EmpleadoNombre':"Nombre de Empleado:",
                  'EmpleadoEdad':"Edad del empleado"}
        widget={'idEmpleado':forms.TextInput,
                'EmpleadoNombre': forms.TextInput,
                'EmpleadoEdad': forms.TextInput
        }

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = ['idProveedor', 'nombreProveedor']
        labels = {'idProveedor':"codigo de proveedor:",
                  'nombreProveedor':"Nombre de Proveedor:",
                  }
        widget={'idProveedor':forms.TextInput,
                'nombreProveedor': forms.TextInput,
                
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['idProducto', 'nombreProducto']
        labels = {'idProducto':"codigo de producto:",
                  'nombreProducto':"Nombre de producto:",
                  }
        widget={'idProducto':forms.TextInput,
                'nombreProducto': forms.TextInput,
                
        }

class clienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['idCliente', 'nombreCliente']
        labels = {'idCliente':"codigo de Cliente:",
                  'nombreCliente':"Nombre de Cliente:",
                  }
        widget={'idCliente':forms.TextInput,
                'nombreCliente': forms.TextInput,
                
        }

class facturaForm(forms.ModelForm):
    class Meta:
        model = Facturas
        fields = ['idFactura', 'nombreCliente']
        labels = {'idFactura':"codigo de Factura:",
                  'nombreCliente':"Nombre de Cliente:",
                  }
        widget={'idFactura':forms.TextInput,
                'nombreCliente': forms.TextInput,
                
        }
        
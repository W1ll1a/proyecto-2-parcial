from django import forms
from .models import Empleados

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = ['idEmpleado', 'EmpleadoNombre']
        labels = {'idEmpleado':"codigo de empleado:",
                  'EmpleadoNombre':"Nombre de Empleado:"}
        widget={'idEmpleado':forms.TextInput,
                'EmpleadoNombre': forms.TextInput
        }
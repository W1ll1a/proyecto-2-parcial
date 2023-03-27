from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Empleados(models.Model):
    idEmpleado = models.IntegerField(primary_key=True)
    EmpleadoNombre = models.CharField(max_length=50)
    EmpleadoEdad= models.SmallIntegerField(null=False)
    EmpleadoTel = models.CharField(validators=[RegexValidator(r'^\d+$', message='Only numbers are allowed.')],max_length=8)
    EmpleadoSalario= models.IntegerField(null=False)
    EmpleadoCorreo= models.EmailField(null=False)
    def __str__(self) :
        return str(self.idEmpleado)+ " "  + self.EmpleadoNombre + " "+ str(self.EmpleadoEdad)


class Proveedores(models.Model):
    idProveedor=models.IntegerField(primary_key=True)
    nombreProveedor= models.CharField(max_length=50)
    ProveedorDireccion= models.CharField(max_length=100)
    ProveedorTelefono= models.CharField(validators=[RegexValidator(r'^\d+$', message='Only numbers are allowed.')],max_length=8)
    ProveedorCorreo= models.EmailField(null=False)

    def __str__(self):
        return str(self.idProveedor) + " " + self.nombreProveedor
    
class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True)
    nombreProducto = models.CharField(max_length=50)
    idProveedor = models.ForeignKey(Proveedores,null=False, blank=False, on_delete=models.PROTECT  )
    ProductoDescripcion= models.CharField(max_length=100)
    ProductoPrecio= models.IntegerField(null=False)
    Inventario= models.IntegerField(null=False)
    

    
    def __str__(self):
        return str(self.idProducto) + " " + self.nombreProducto
    
    
class Cliente(models.Model):
     idCliente=models.IntegerField(primary_key=True)
     nombreCliente= models.CharField(max_length=50)
     ClienteTelefono= models.CharField(validators=[RegexValidator(r'^\d+$', message='Only numbers are allowed.')],max_length=8)
     ClienteCorreo= models.EmailField(null=False)
     

     def __str__(self):
        return str(self.idCliente) + " " + self.nombreCliente
    
class Facturas(models.Model):
    idFactura= models.IntegerField(primary_key=True)
    nombreCliente=models.ForeignKey(Cliente,null=False, blank=False, on_delete=models.PROTECT)
    idProducto=models.ForeignKey(Producto,null=False, blank=False, on_delete=models.PROTECT)
    idEmpleado=models.ForeignKey(Empleados,null=False, blank=False, on_delete=models.PROTECT)
    Subtotal= models.IntegerField(null=False)
    Total= models.IntegerField(null=False)
    MetodoPago= models.CharField(max_length=20)
    
    
    def __str__(self) :
        return str(self.idFactura)+ " "  + self.nombreCliente    


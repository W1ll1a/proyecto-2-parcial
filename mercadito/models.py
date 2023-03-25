from django.db import models

# Create your models here.
class Empleados(models.Model):
    idEmpleado = models.IntegerField(primary_key=True)
    EmpleadoNombre = models.CharField(max_length=50)
    EmpleadoEdad= models.SmallIntegerField()
    

    def __str__(self) :
        return str(self.idEmpleado)+ " "  + self.EmpleadoNombre + " "+ str(self.EmpleadoEdad)

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True)
    nombreProducto = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.idProducto) + " " + self.nombreProducto
    
class Proveedores(models.Model):
    idProveedor=models.IntegerField(primary_key=True)
    nombreProveedor= models.CharField(max_length=50)

    def __str__(self):
        return str(self.idProveedor) + " " + self.nombreProveedor
    
class Cliente(models.Model):
     idCliente=models.IntegerField(primary_key=True)
     nombreCliente= models.CharField(max_length=50)

     def __str__(self):
        return str(self.idCliente) + " " + self.nombreCliente
    
class Facturas(models.Model):
    idFactura= models.IntegerField(primary_key=True)
    nombreCliente=models.ForeignKey(Cliente,null=False, blank=False, on_delete=models.PROTECT)
    
    
    


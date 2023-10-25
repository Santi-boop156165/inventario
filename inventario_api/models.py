from django.db import models

# Create your models here.
class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    proveedor_id = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

class Almacen(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    productos_id = models.ManyToManyField(Producto, through='Inventario')

class Inventario(models.Model):
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    almacen_id = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

class Transaccion(models.Model):
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_id = models.IntegerField()
    tipo = models.CharField(max_length=50) 
    fecha = models.DateTimeField(auto_now_add=True)
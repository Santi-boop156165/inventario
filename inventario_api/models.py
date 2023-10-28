from django.db import models

# Create your models here.
class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100) 
    precio = models.DecimalField(max_digits=10, decimal_places=2) 
    proveedor_id = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

class Almacen(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    capacidad_total = models.IntegerField() 
    capacidad_actual = models.IntegerField()
    productos_id = models.ManyToManyField(Producto, through='Inventario')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.capacidad_actual = self.capacidad_total
        super(Almacen, self).save(*args, **kwargs)

class Inventario(models.Model):
    id = models.AutoField(primary_key=True)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    almacen_id = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True) 
    cantidad_de_producto = models.IntegerField() 
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)  

class Transaccion(models.Model):
    id = models.AutoField(primary_key=True)
    inventario_id = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    cantidad= models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
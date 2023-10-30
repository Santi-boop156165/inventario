from rest_framework import serializers
from .models import Proveedor, Producto, Almacen, Inventario, Transaccion

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    proveedor = ProveedorSerializer(read_only=True)
    class Meta:
        model = Producto
        fields = '__all__'

class AlmacenSerializer(serializers.ModelSerializer):
    capacidad_actual = serializers.IntegerField(required=False)
    class Meta:
        model = Almacen
        fields = '__all__'

class InventarioSerializer(serializers.ModelSerializer):
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)

    class Meta:
        model = Inventario
        fields = '__all__'

class TransaccionSerializer(serializers.ModelSerializer):
    total = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    class Meta:
        model = Transaccion
        fields = '__all__'
    
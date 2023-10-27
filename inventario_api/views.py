from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Proveedor,Producto,Almacen,Inventario,Transaccion
from .serializers import ProveedorSerializer,ProductoSerializer,AlmacenSerializer,InventarioSerializer,TransaccionSerializer
from rest_framework import status
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F
# Create your views here.

class ProvedorApiView(APIView):

    def get(self, request): #busqueda por id y verificar que en los casos de uso tenga errores coherentes 
        provedor = Proveedor.objects.all()
        serializer = ProveedorSerializer(provedor, many=True)
        return Response({"message" :"succes","provedores": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request): #verificar que en los casos de uso tenga errores coherentes
        serializer = ProveedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Proveedor creado correctamente"   }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id): #verificar que en los casos de uso tenga errores coherentes
        provedor = Proveedor.objects.get(id=id)
        serializer = ProveedorSerializer(provedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Proveedor actualizado correctamente"   }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id): #verificar que en los casos de uso tenga errores coherentes
        provedor = Proveedor.objects.get(id=id)
        provedor.delete()
        return Response({"message": "Proveedor eliminado correctamente"   }, status=status.HTTP_200_OK)
    
class ProductoApiView(APIView):

    def get(self, request): #busqueda por id y verificar que en los casos de uso tenga errores coherentes
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many=True)
        return Response({"message" :"succes","productos": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request): #verificar que en los casos de uso tenga errores coherentes
        proveedor_id = request.data.get('proveedor_id')
        try:
            Proveedor.objects.get(id=proveedor_id)
        except ObjectDoesNotExist:
            return Response({"message": "Proveedor no encontrado"}, status=status.HTTP_400_BAD_REQUEST)
    
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Producto creado correctamente"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id): #verificar que en los casos de uso tenga errores coherentes
        producto = Producto.objects.get(id=id)
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Producto actualizado correctamente"   }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id): #verificar que en los casos de uso tenga errores coherentes
        producto = Producto.objects.get(id=id)
        producto.delete()
        return Response({"message": "Producto eliminado correctamente"   }, status=status.HTTP_200_OK)
    
class AlmacenApiView(APIView):

    def get(self, request): #busqueda por id y verificar que en los casos de uso tenga errores coherentes
        almacen = Almacen.objects.all()
        serializer = AlmacenSerializer(almacen, many=True)
        return Response({"message" :"succes","almacenes": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request): #verificar que en los casos de uso tenga errores coherentes
        serializer = AlmacenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Almacen creado correctamente"   }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # crear metodo put y deleate
    
class InventariosApiView(APIView):

    def get(self, request): #busqueda por id y verificar que en los casos de uso tenga errores coherentes
        inventario = Inventario.objects.all()
        serializer = InventarioSerializer(inventario, many=True)
        return Response({"message" :"succes","inventarios": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request): #verificar que en los casos de uso tenga errores coherentes
        serialezer = InventarioSerializer(data=request.data)
        if serialezer.is_valid():

            producto_id = serialezer.validated_data.get('producto_id').id
            producto = Producto.objects.get(id=producto_id)

            almacen_id = request.data.get('almacen_id')
            almacen = Almacen.objects.get(id=almacen_id)

            cantidad = serialezer.validated_data.get('cantidad_de_producto')
            subtotal = cantidad * producto.precio

            serialezer.validated_data['subtotal'] = subtotal

            if almacen.capacidad_actual >= cantidad:
                with transaction.atomic():

                    serialezer.save()
                    almacen.capacidad_actual = F('capacidad_actual') - cantidad
                    almacen.save()
                    
                return Response({"message": "Inventario creado correctamente"   }, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "No hay suficiente espacio en el almacen"   }, status=status.HTTP_400_BAD_REQUEST)
        return Response(serialezer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        # crear metodo put y deleate
        
    
class TransaccionApiView(APIView):

    def get(self, request):
        transaccion = Transaccion.objects.all()
        serializer = TransaccionSerializer(transaccion, many=True)
        return Response({"message" :"succes","transacciones": serializer.data}, status=status.HTTP_200_OK) 
    

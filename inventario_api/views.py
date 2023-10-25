from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Proveedor,Producto,Almacen,Inventario,Transaccion
from .serializers import ProveedorSerializer,ProductoSerializer,AlmacenSerializer,InventarioSerializer,TransaccionSerializer
from rest_framework import status
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

class ProvedorApiView(APIView):

    def get(self, request):
        provedor = Proveedor.objects.all()
        serializer = ProveedorSerializer(provedor, many=True)
        return Response({"message" :"succes","provedores": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ProveedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Proveedor creado correctamente"   }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        provedor = Proveedor.objects.get(id=id)
        serializer = ProveedorSerializer(provedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Proveedor actualizado correctamente"   }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        provedor = Proveedor.objects.get(id=id)
        provedor.delete()
        return Response({"message": "Proveedor eliminado correctamente"   }, status=status.HTTP_200_OK)
    
class ProductoApiView(APIView):

    def get(self, request):
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many=True)
        return Response({"message" :"succes","productos": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
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
    
    def put(self, request, id):
        producto = Producto.objects.get(id=id)
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Producto actualizado correctamente"   }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        producto = Producto.objects.get(id=id)
        producto.delete()
        return Response({"message": "Producto eliminado correctamente"   }, status=status.HTTP_200_OK)
    
class AlmacenApiView(APIView):

    def get(self, request):
        almacen = Almacen.objects.all()
        serializer = AlmacenSerializer(almacen, many=True)
        return Response({"message" :"succes","almacenes": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = AlmacenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Almacen creado correctamente"   }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class InventariosApiView(APIView):

    def get(self, request):
        inventario = Inventario.objects.all()
        serializer = InventarioSerializer(inventario, many=True)
        return Response({"message" :"succes","inventarios": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = InventarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Inventario creado correctamente"   }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TransaccionApiView(APIView):

    def get(self, request):
        transaccion = Transaccion.objects.all()
        serializer = TransaccionSerializer(transaccion, many=True)
        return Response({"message" :"succes","transacciones": serializer.data}, status=status.HTTP_200_OK)
    
    @transaction.atomic  
    def post(self, request):
        serializer = TransaccionSerializer(data=request.data)
        if serializer.is_valid():
            producto_id = serializer.validated_data.get('producto_id').id
            cantidad = serializer.validated_data.get('cantidad_id')
            tipo = serializer.validated_data.get('tipo')
            
  
            try:
                inventario = Inventario.objects.get(producto_id=producto_id)
            except ObjectDoesNotExist:
                return Response({"message": "Inventario para el producto no encontrado"},
                                status=status.HTTP_400_BAD_REQUEST)
            

            if tipo == 'Compra':
                inventario.cantidad += cantidad
            elif tipo == 'Venta':
                if inventario.cantidad < cantidad:
                    return Response({"message": "Stock insuficiente"},
                                    status=status.HTTP_400_BAD_REQUEST)
                inventario.cantidad -= cantidad
            else:
                return Response({"message": "Tipo de transacción no válido"},
                                status=status.HTTP_400_BAD_REQUEST)
            

            inventario.save()
            serializer.save()
            
            return Response({"message": "Transacción creada correctamente"},
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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

    def get(self, request, id=0): #busqueda por id y verificar que en los casos de uso tenga errores coherentes 
        if id>0:
            try:
                provedor=Proveedor.objects.get(id=id)
                serializer=ProveedorSerializer(provedor)
                data={
                    "message":"Proveedor encontrado",
                    "proveedor":serializer.data
                }
                return Response(data, status=status.HTTP_200_OK)
            except Proveedor.DoesNotExist:
                return Response({"message":"Proveedor no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
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

    def get(self, request, id=0): #busqueda por id y verificar que en los casos de uso tenga errores coherentes
        if id>0:
            try:
                producto=Producto.objects.get(id=id)
                serializer=ProductoSerializer(producto)
                data={
                    "message":"Producto encontrado",
                    "producto":serializer.data
                }
                return Response(data, status=status.HTTP_200_OK)
            except Producto.DoesNotExist:
                return Response({"message":"Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
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

    def get(self, request, id=0): #busqueda por id y verificar que en los casos de uso tenga errores coherentes
        if id>0:
            try:
                almacen=Almacen.objects.get(id=id)
                serializer=AlmacenSerializer(almacen)
                data={
                    "message":"almacen encontrado",
                    "almacen":serializer.data
                }
                return Response(data, status=status.HTTP_200_OK)
            except Almacen.DoesNotExist:
                return Response({"message":"Almacen no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            almacen = Almacen.objects.all()
            serializer = AlmacenSerializer(almacen, many=True)
            return Response({"message" :"succes","almacenes": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request): #verificar que en los casos de uso tenga errores coherentes
        serializer = AlmacenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Almacen creado correctamente"   }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id): #verificar que en los casos de uso tenga errores coherentes
        almacen = Almacen.objects.get(id=id)
        serializer = AlmacenSerializer(almacen, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Almacen actualizado correctamente"   }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id): #verificar que en los casos de uso tenga errores coherentes
        almacen = Almacen.objects.get(id=id)
        almacen.delete()
        return Response({"message": "Almacen eliminado correctamente"   }, status=status.HTTP_200_OK)
    
    # crear metodo put y deleate
    
class InventariosApiView(APIView):

    def get(self, request, id=0): #busqueda por id y verificar que en los casos de uso tenga errores coherentes
        if id>0:
            try:
                inventario=Inventario.objects.get(id=id)
                serializer=InventarioSerializer(inventario)
                data={
                    "message":"Inventario encontrado",
                    "inventario": serializer.data
                }
                return Response(data, status=status.HTTP_200_OK)
            except Inventario.DoesNotExist:
                return Response({"message":"Inventario no encontrado"}, status=status.HTTP_404_NOT_FOUND)    
        else:
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
    
    def put (self, request, id):
        inventario = Inventario.objects.get(id=id)
        cantidad_actual=inventario.cantidad_de_producto
        
        almacen_id=inventario.almacen_id.id
        producto_actual=inventario.producto_id
        serialezer = InventarioSerializer(inventario, data=request.data)
        if serialezer.is_valid():
            nueva_cantidad=serialezer.validated_data.get('cantidad_de_producto')
            nuevo_almacen_id=serialezer.validated_data.get('almacen_id').id
            
            nuevo_producto=serialezer.validated_data.get('producto_id').id
            producto=Producto.objects.get(id=nuevo_producto)
            sub_total_nuevo=nueva_cantidad * producto.precio
            print(sub_total_nuevo)
            almacen=Almacen.objects.get(id=nuevo_almacen_id)
            
            if almacen.capacidad_actual+cantidad_actual >=nueva_cantidad:
                with transaction.atomic():
                    serialezer.validated_data['subtotal']=sub_total_nuevo
                    if almacen_id != nuevo_almacen_id:
                        almacen_actual=Almacen.objects.get(id=almacen_id)
                        almacen_actual.capacidad_actual=F('capacidad_actual') + cantidad_actual
                        almacen_actual.save() 
                    almacen.capacidad_actual=F('capacidad_actual') + cantidad_actual - nueva_cantidad
                    almacen.save()
                    serialezer.save()
                return Response({"message": "Inventario actualizado correctamente"   }, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "No hay suficiente espacio en el almacen"   }, status=status.HTTP_400_BAD_REQUEST)
        return Response(serialezer.errors, status=status.HTTP_400_BAD_REQUEST)        
        
    
    def delete(self, request, id): #verificar que en los casos de uso tenga errores coherentes
        try:
            inventario=Inventario.objects.get(id=id)
            cantidad_inventario=inventario.cantidad_de_producto
            almacen_inventario=inventario.almacen_id
            with transaction.atomic():
                almacen_inventario.capacidad_actual= F('capacidad_actual') + cantidad_inventario
                almacen_inventario.save()
                inventario.delete()
            return Response({"message": "Se elimino el inventario"}, status=status.HTTP_200_OK)    
        except Inventario.DoesNotExist:
            return Response({"message": "El inventario no se encontro"}, status=status.HTTP_400_BAD_REQUEST)
        
class TransaccionApiView(APIView):

    def get(self, request):
        transaccion = Transaccion.objects.all()
        serializer = TransaccionSerializer(transaccion, many=True)
        return Response({"message" :"succes","transacciones": serializer.data}, status=status.HTTP_200_OK) 
    
        

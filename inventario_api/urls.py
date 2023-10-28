from django.urls import path
from .views import ProvedorApiView, ProductoApiView, AlmacenApiView,InventariosApiView,TransaccionApiView

urlpatterns = [
    path('provedores', ProvedorApiView.as_view(), name="listar_provedores"),
    path('provedores/<int:id>', ProvedorApiView.as_view(), name="procesar_provedores"),
    path('productos', ProductoApiView.as_view(), name="listar_productos"),
    path('productos/<int:id>', ProductoApiView.as_view(), name="procesar_productos"),
    path('almacenes', AlmacenApiView.as_view(), name="listar_almacenes"),
    path('almacenes/<int:id>', AlmacenApiView.as_view(), name="procesar_almacenes"),
    path('inventarios', InventariosApiView.as_view(), name="listar_inventarios"),
    path('inventarios/<int:id>', InventariosApiView.as_view(), name="procesar_inventarios"),
    path('transacciones', TransaccionApiView.as_view(), name="listar_transacciones"),


]
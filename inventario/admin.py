from django.contrib import admin
from .models import Proveedor, Empleado, Bodega, Producto, Compra, Embalaje, Cliente, Venta, VentaProducto
# Register your models here.
admin.site.register(Proveedor)
admin.site.register(Empleado)
admin.site.register(Bodega)
admin.site.register(Producto)
admin.site.register(Compra)
admin.site.register(Embalaje)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(VentaProducto)
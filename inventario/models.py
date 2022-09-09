from operator import truediv
from django.db import models

# Create your models here.
class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=20)
    telefono = models.CharField(max_length=15)
    correo_electronico = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre_empleado = models.CharField(max_length=20)
    telefono_empleado = models.CharField(max_length=15)
    correo_electronico = models.CharField(max_length=20)
    direccion_empleado = models.CharField(max_length=50)
    puesto_empleado = models.CharField(max_length=15)

class Bodega(models.Model):
    id_bodega = models.AutoField(primary_key=True)
    id_encargado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    nombre_bodega = models.CharField(max_length=20)
    ubicacion = models.CharField(max_length=50)

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    id_bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=20)
    tipo_producto = models.CharField(max_length=10)
    marca_producto = models.CharField(max_length=20)
    fecha_vencimiento = models.DateField(null=False, blank=False)
    def save(self, *args, **kwargs):
        registro = Registro(tipo_transaccion = 'Ingreso', detalle = 'Ingreso de mercaderia al stock por motivo de compra, producto: '+self.nombre_producto)
        registro.save()
        return super(Producto, self).save( *args, **kwargs)
    def delete(self, *args, **kwargs):
        registro = Registro(tipo_transaccion = 'Salida', detalle = 'Salida de mercaderia del stock por motivo de venta, producto: '+self.nombre_producto)
        registro.save()
        return super(Producto, self).delete( *args, **kwargs)

class Compra(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    cantidad_producto = models.IntegerField(null=False, blank=False)

class Embalaje(models.Model):
    id_embalaje = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipo_embalaje = models.CharField(max_length=15)
    proporcion_unidades = models.IntegerField(null=False, blank=False)
    existencias = models.IntegerField(null=False, blank=False)
    precio_venta = models.FloatField(null=False, blank=False)
    precio_compra = models.FloatField(null=False, blank=False)
    def save(self, *args, **kwargs):
        registro = Registro(tipo_transaccion = 'Ingreso', detalle = 'Ingreso de nuevo lote, Tipo embalaje: '+self.tipo_embalaje)
        registro.save()
        return super(Embalaje, self).save( *args, **kwargs)

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=20)
    telefono_cliente = models.CharField(max_length=15)
    correo_electronico = models.CharField(max_length=50)
    nit_cliente = models.CharField(max_length=15)

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    detalle_factura = models.CharField(max_length=300)
    total = models.IntegerField(null=False, blank=False)
    fecha = models.DateField(null=False, blank=False)

class VentaProducto(models.Model):
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_producto = models.IntegerField(null=False, blank=False)

class Registro(models.Model):
    id_registro = models.AutoField(primary_key=True)
    fecha_ocurrencia = models.DateTimeField(auto_now=True)
    tipo_transaccion = models.CharField(max_length=10, null=False)
    detalle = models.CharField(max_length=500, null=False)




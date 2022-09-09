from audioop import add
from math import prod
from sqlite3 import Cursor
from django.shortcuts import render, redirect
from .models import Bodega, Embalaje, Producto, Proveedor, Registro

# Create your views here.
def Home(request):
    product = Producto.objects.all()
    bodega = Bodega.objects.all()
    embalaje = Embalaje.objects.all()
    return render(request, "manageProduct.html", {"products": product, "bodegas": bodega, "embalajes": embalaje})

def Proveedores(request):
    provider = Proveedor.objects.all()
    return render(request, "manageProvider.html", {"provider": provider})

def Registros(request):
    reg = Registro.objects.all()
    return render(request, "kardex.html", {"kardex": reg})

def AddProduct(request):
    bodega = Bodega.objects.get(id_bodega = request.POST['idBodega'])
    name = request.POST['txtName']
    tipo = request.POST['txtTipo']
    marca = request.POST['txtMarca']
    fecha = request.POST['txtFecha']
    product = Producto(id_bodega = bodega,nombre_producto = name, tipo_producto = tipo, marca_producto = marca, fecha_vencimiento = fecha)
    
    product.save()
    return redirect('/')

def AddEmb(request):
    prod = Producto.objects.get(id_producto = request.POST['id_prod'] )
    tipo_emb = request.POST['tipo_emb']
    proporcion = request.POST['proporcion']
    existencias = request.POST['existencias']
    precio_venta = request.POST['precio_venta']
    precio_compra = request.POST['precio_compra']
    embalaje = Embalaje(id_producto = prod,tipo_embalaje = tipo_emb, proporcion_unidades = proporcion, existencias = existencias, precio_venta = precio_venta, precio_compra = precio_compra)

    embalaje.save()
    return redirect('/')


def DeleteProduct(request, id):
    product = Producto.objects.get(id_producto = id)
    product.delete()
    return redirect('/')

def EditProduct(request, id):
    product = Producto.objects.get(id_producto = id)
    bodega = Bodega.objects.all()
    return render(request, "editProduct.html", {"product": product, "bodegas" : bodega})

def UpdateProduct(request):
    bodega = Bodega.objects.get(id_bodega = request.POST['idBodega'])
    id = request.POST['txtId']
    name = request.POST['txtName']
    tipo = request.POST['txtTipo']
    marca = request.POST['txtMarca']
    fecha = request.POST['txtFecha']
    product = Producto.objects.get(id_producto = id)
    product.id_bodega = bodega
    product.nombre_producto = name
    product.tipo_producto = tipo
    product.marca_producto = marca
    product.fecha_vencimiento = fecha
    product.save()
    return redirect('/')


def AddProvider(request):
    name = request.POST['name']
    phone = request.POST['telefono']
    mail = request.POST['correo']
    address = request.POST['direccion']
    provider = Proveedor(nombre_proveedor = name, telefono = phone, correo_electronico = mail, direccion = address)
    provider.save()
    return redirect('/proveedores')

def DeleteProvider(request, id):
    provider = Proveedor.objects.get(id_proveedor = id)
    provider.delete()
    return redirect('/proveedores')

def EditProvider(request, id):
    provider = Proveedor.objects.get(id_proveedor = id)
    return render(request, "editProvider.html", {"provider": provider})

def UpdateProvider(request):
    id = request.POST['id']
    name = request.POST['name']
    cel = request.POST['telefono']
    mail = request.POST['correo']
    address = request.POST['direccion']
    provider = Proveedor.objects.get(id_proveedor = id)
    provider.nombre_proveedor = name
    provider.telefono = cel
    provider.correo_electronico = mail
    provider.direccion = address
    provider.save()
    return redirect('/proveedores')


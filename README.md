# Ferreteria Application (CRUD)

Esta aplicación consiste en el desarrollo y documentación de una aplicacion para llevar el control de las ventas, compras y mercaderías de una ferretería.

La aplicación está desarrollada con ayuda de las siguientes tecnologias:

|Herramienta| Version |
|-------- |-------- |
|Python   | v3.10.5 |
|Django   | v4.1.1  |
|PostgreSQL | v14.4.1 |
|Bootstrap | v5.2.1 |
|app.diagrams.net | v20.3.0 |

La aplicación se desarrolló en base a los siguientes tres incisos:

1) #### Crear un diagrama de entidad de relación para un módulo de compras, ventas, bodegas e inventario:

![](https://i.imgur.com/qzEwEdT.png)

2) #### Crear un CRUD para el proceso de inventario dentro de una bodega:

La aplicación consta de varios modulos de  como bodega, compra, venta, proveedores y una sección de registro (Kardex). Cada sección cuenta con a opcion de Agregar, Leer, Editar y eliminar un registro.

![](https://i.imgur.com/jLYbnG8.png)

Para el ingreso un producto es necesario ingresar la bodega donde se ubica, el nombre del producto, el tipo (producto o servicio), marca y fecha de vencimiento.

![](https://i.imgur.com/tPvyhUt.png)

A través de los botones Cambio y Salida se puede editar y eliminar un registro.

![](https://i.imgur.com/BA0iz0H.png)

El embalaje se manejo con el llenado de un formulario, donde indica el nivel, el precio la unidad, etc. para luego mostrarse en la lista de productos.

![](https://i.imgur.com/DiYxTPF.png)

El ingreso de proveedores se realiza en la siguiente pestaña.

![](https://i.imgur.com/UVnOmXm.png)


4) #### Debe existir un detalle de los ingresos y salidas de la mercadería, así como un numero de documento que justifique el tipo de transacción.

En la pestaña de Ingresos y salidas se puede revisar el historial de los movimientos de los productos.

![](https://i.imgur.com/XsI12Xp.png)

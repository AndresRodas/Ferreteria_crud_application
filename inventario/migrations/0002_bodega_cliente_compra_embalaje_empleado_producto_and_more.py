# Generated by Django 4.1.1 on 2022-09-09 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id_bodega', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_bodega', models.CharField(max_length=20)),
                ('ubicacion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(max_length=20)),
                ('telefono_cliente', models.CharField(max_length=15)),
                ('correo_electronico', models.CharField(max_length=50)),
                ('nit_cliente', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_producto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Embalaje',
            fields=[
                ('id_embalaje', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_embalaje', models.CharField(max_length=15)),
                ('proporcion_unidades', models.IntegerField()),
                ('existencias', models.IntegerField()),
                ('precio_venta', models.IntegerField()),
                ('precio_compra', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_empleado', models.CharField(max_length=20)),
                ('telefono_empleado', models.CharField(max_length=15)),
                ('correo_electronico', models.CharField(max_length=20)),
                ('direccion_empleado', models.CharField(max_length=50)),
                ('puesto_empleado', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=20)),
                ('tipo_producto', models.CharField(max_length=10)),
                ('marca_producto', models.CharField(max_length=20)),
                ('fecha_vencimiento', models.DateField()),
                ('id_bodega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.bodega')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_proveedor', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=15)),
                ('correo_electronico', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False)),
                ('detalle_factura', models.CharField(max_length=300)),
                ('total', models.IntegerField()),
                ('fecha', models.DateField()),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.cliente')),
                ('id_empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='VentaProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_producto', models.IntegerField()),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.producto')),
                ('id_venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.venta')),
            ],
        ),
        migrations.DeleteModel(
            name='Proveedores',
        ),
        migrations.AddField(
            model_name='embalaje',
            name='id_producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.producto'),
        ),
        migrations.AddField(
            model_name='compra',
            name='id_producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.producto'),
        ),
        migrations.AddField(
            model_name='compra',
            name='id_proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.proveedor'),
        ),
        migrations.AddField(
            model_name='bodega',
            name='id_encargado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.empleado'),
        ),
    ]
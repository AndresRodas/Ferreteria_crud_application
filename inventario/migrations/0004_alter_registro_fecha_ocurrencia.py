# Generated by Django 4.1.1 on 2022-09-09 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_registro_alter_embalaje_precio_compra_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='fecha_ocurrencia',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

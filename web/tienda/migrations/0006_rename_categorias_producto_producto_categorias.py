# Generated by Django 5.0 on 2023-12-16 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0005_rename_categorias_producto_categorias_producto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='categorias_producto',
            new_name='categorias',
        ),
    ]

# Generated by Django 5.0 on 2023-12-12 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_remove_producto_articulo_producto_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='tienda'),
        ),
    ]

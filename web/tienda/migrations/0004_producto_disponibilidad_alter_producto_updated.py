# Generated by Django 5.0 on 2023-12-12 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_alter_categoria_updated_alter_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='disponibilidad',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

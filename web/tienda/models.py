from django.db import models

# Create your models here.

class categoria(models.Model):
    nombre = models.CharField(max_length=20)
    created= models.DateField(auto_now_add=True)
    updated= models.DateField(auto_now_add=True)
    
    
class producto(models.Model):
    
    articulo    = models.CharField(max_length=20)
    precio      = models.IntegerField()
    categorias  = models.ManyToManyField(categoria)
    imagen      = models.ImageField(upload_to="productos")
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now_add=True)
    
    
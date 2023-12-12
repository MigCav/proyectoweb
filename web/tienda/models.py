from django.db import models

# Create your models here.

class categoria(models.Model):
    nombre = models.CharField(max_length=20)
    created= models.DateField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre
    
    class meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
    
    
class producto(models.Model):
    
    codigo      = models.IntegerField(default=0)
    precio      = models.IntegerField()
    categorias  = models.ManyToManyField(categoria)
    imagen      = models.ImageField(upload_to="tienda")
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now_add=True)
    
    class meta:
        verbose_name = "producto"
        verbose_name_plural = "productoss"
    
    def __str__(self):
        return str(self.codigo    )

from django.shortcuts import render
from .models import categoria, producto
# Create your views here.

def tienda(request):
    
    productos  = producto.objects.all()
    categoriastienda = categoria.objects.all()
        
    return render(request, "tienda/tienda.html", {"categorias":categoriastienda, "productos":productos})


def categoria_tienda(request, categorias_id):
    
    Categorias = categoria.objects.get(id = categorias_id)
    productos = producto.objects.filter(categorias = Categorias)
    categorias = categoria.objects.all()
    
    return render(request,'tienda/categoriad.html', {'Categorias': Categorias, 'productos':productos, 'categorias':categorias} )
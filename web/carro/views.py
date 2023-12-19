from django.shortcuts import render

from .carro import Carro
from tienda.models import producto
from django.shortcuts import redirect
# Create your views here.

def agregar_producto(request, producto_id):
    
    carro = Carro(request)
    
    producto_carro = producto.objects.get(producto_id)
    
    carro.agregar(producto=producto_carro)
     
    return redirect('tienda')

def eliminar_producto(request, producto_id):
    
    carro = Carro(request)
    
    producto_carro = producto.objects.get(producto_id)
    
    carro.eliminar(producto=producto_carro)
     
    return redirect('tienda')

def restar_producto(request, producto_id):
    
    carro = Carro(request)
    
    producto_carro = producto.objects.get(producto_id)
    
    carro.restar_productos(producto=producto_carro)
     
    return redirect('tienda')

def limpiar_carro(request, producto_id):
    
    carro = Carro(request)
    
    carro.limpiar_carro()
    return redirect('tienda')
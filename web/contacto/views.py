from django.shortcuts import render

from .forms import form_contacto


# Create your views here.

def contacto(request):
    
    formulario_contacto = form_contacto()
    
    return render(request, "contacto/contacto.html", {'form_contacto':formulario_contacto} )


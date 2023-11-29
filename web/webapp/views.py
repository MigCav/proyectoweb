from django.shortcuts import render,HttpResponse

from servicios.models import servicio


# Create your views here.

def home(request):
    
    return render(request, "webapp/home.html")

def tienda(request):
    
    return render(request, "webapp/tienda.html")

def contacto(request):
    
    return render(request, "webapp/contacto.html")

def blog(request):
    
    return render(request, "webapp/blog.html")

def servicios(request):
    
    servicios = servicio.objects.all()
        
    return render(request, "webapp/servicios.html", {"servicios":servicios})



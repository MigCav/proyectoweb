from django.shortcuts import render,HttpResponse


def home(request):
    
    return render(request, "webapp/home.html")

def tienda(request):
    
    return render(request, "webapp/tienda.html")

def contacto(request):
    
    return render(request, "webapp/contacto.html")

def blog(request):
    
    return render(request, "webapp/blog.html")

def servicios(request):
    
    return render(request, "webapp/servicios.html")

# Create your views here.

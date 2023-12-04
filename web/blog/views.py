from django.shortcuts import render
from .models import post, categoria

# Create your views here.

def blog(request):
    
    posts = post.objects.all()
    categorias = categoria.objects.all()
    
    return render(request, "blog/blog.html", {'posts':posts, 'categorias':categorias})

def categorias(request, categorias_id):
        
    categorias  = categoria.objects.get(id = categorias_id)
    posts       = post.objects.filter(categoria = categorias)
    Categorias  =categoria.objects.all()
    
    return render(request, "blog/categorias.html", {'categoria':categorias, 'posts':posts, 'Categorias':Categorias})
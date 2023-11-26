from django.urls import path

from webapp import views

urlpatterns = [
    path("home/", views.home),
    path("tienda/", views.tienda),
    path("blog/", views.blog),
    path("servicios/", views.servicios),
    path("contacto/", views.contacto),
    
    
]
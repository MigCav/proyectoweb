from django.urls import path

from webapp import views

urlpatterns = [
    path("home/", views.home, name='home'),
    path("tienda/", views.tienda, name='tienda'),
    path("blog/", views.blog, name='blog'),
    path("servicios/", views.servicios, name= 'servicios'),
    path("contacto/", views.contacto, name='contacto'),
    
    
]
from django.urls import path

from webapp import views

urlpatterns = [
    path("", views.home, name='Home'),
    path("tienda/", views.tienda, name='Tienda'),
    path("blog/", views.blog, name='Blog'),
    path("servicios/", views.servicios, name= 'Servicios'),
    path("contacto/", views.contacto, name='Contacto'),
    
    
]
from django.urls import path

from . import views

urlpatterns = [
    path("", views.tienda, name='Tienda'),
    path("categoriad/<int:categorias_id>", views.categoria_tienda, name='categoriat'),
    
    
]
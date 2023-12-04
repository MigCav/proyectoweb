from django.urls import path
from . import views


urlpatterns = [
    path("", views.blog, name='Blog'),
    path("categorias/<int:categorias_id>", views.categorias, name='categorias'),
 
]

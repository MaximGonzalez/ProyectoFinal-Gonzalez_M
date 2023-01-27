from django.contrib import admin, staticfiles
from django.urls import path
from .views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("usuarios/", usuarios, name="usuarios"),
    path("posteos/", posteos, name="posteos"),
    path("comentarios/", comentarios, name="comentarios"),
    path("crearposteos/", crear_posteos, name="crear_posteos"),
    path("crearusuarios/", crear_usuarios, name="crear_usuarios"),
    path("buscarposteos/", buscar_posteos, name="buscar_posteos"),
    path("crearocomentario/", crear_comentario, name="crear_comentario"),
]
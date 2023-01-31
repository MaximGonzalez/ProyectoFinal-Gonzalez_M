from django.contrib import admin, staticfiles
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from .views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("usuarios/", usuarios, name="usuarios"),
    path("posteos/", posteos, name="posteos"),
    path("comentarios/", comentarios, name="comentarios"),
    path("crearposteos/", crear_posteo, name="crear_posteo"),
    path("crearusuarios/", crear_usuarios, name="crear_usuarios"),
    path("buscarposteos/", buscar_posteos, name="buscar_posteos"),
    path("crearocomentario/", crear_comentario, name="crear_comentario"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
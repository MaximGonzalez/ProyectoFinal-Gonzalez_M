from django.contrib import admin, staticfiles
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from blog_app import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("usuarios/", views.usuarios, name="usuarios"),
    path("post/", views.post, name="post"),
    path("crearpost/", views.crear_post, name="crear_post"),
    path("post/<int:post_id>/", views.post_detalle, name="post_detalle"),
    path("post/<int:post_id>/borrar", views.borrar_post, name="borrar_post"),
    path("buscarposteos/", views.buscar_posteo, name="buscar_posteos"),
    #path("crearocomentario/", views.crear_comentario, name="crear_comentario"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
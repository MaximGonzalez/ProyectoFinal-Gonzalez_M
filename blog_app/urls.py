from django.contrib import admin, staticfiles
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from blog_app import views


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("post/", views.post, name="post"),
    path("crearpost/", views.crear_post, name="crear_post"),
    path("<int:post_id>/", views.post_detalle, name="post_detalle"),
    path("post/<int:post_id>/borrar/", views.borrar_post, name="borrar_post"),
    path("post/<int:post_id>/editar/", views.post_editar, name="post_editar"),
    path("buscarposteos/", views.buscar_posteo, name="buscar_posteos"),
    path("about/", views.about, name="about"),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



class Post(models.Model):
    titulo = models.CharField(max_length=64)
    contenido = RichTextField(blank=True, null=True, config_name='default')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='portadas', null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} | De: {self.usuario}"



class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = RichTextField(blank=True, null=True, config_name='coment_ckeditor')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario por {self.autor} en {self.fecha_publicacion}: {self.comentario}"
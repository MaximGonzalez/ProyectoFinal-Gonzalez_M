from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.
class Usuario(models.Model):
    usuario = models.CharField(max_length=64)
    contrasenia = models.CharField(max_length=64)
    mail = models.EmailField()
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.usuario}"


class Post(models.Model):
    titulo = models.CharField(max_length=64)
    contenido = RichTextField(blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} | De: {self.usuario}"

class Comentario(models.Model):
    texto = models.CharField(max_length=256)
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default='1')
from django.forms import ModelForm
from blog_app.models import Post, Comentario
from django.contrib.auth.models import User
from django import forms




class Crear_post_form(ModelForm):
    class Meta:
        model = Post
        fields = ['titulo',
        'contenido', 'imagen'
        ]



class Crear_comentario_form(ModelForm):
    class Meta:
        model = Comentario
        fields = ['comentario'
        ]





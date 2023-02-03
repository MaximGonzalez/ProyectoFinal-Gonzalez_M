from django.forms import ModelForm
from blog_app.models import Post, Comentario




class Crear_post_form(ModelForm):
    class Meta:
        model = Post
        fields = ['titulo',
        'contenido'
        ]



class Crear_comentario_form(ModelForm):
    class Meta:
        model = Comentario
        fields = ['comentario'
        ]
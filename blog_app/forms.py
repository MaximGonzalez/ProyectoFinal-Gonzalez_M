from django.forms import ModelForm
from blog_app.models import Post




class Crear_post_form(ModelForm):
    class Meta:
        model = Post
        fields = ['titulo',
        'contenido'
        ]



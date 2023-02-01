from django.contrib import admin
from .models import Post, Comentario, Usuario

# Register your models here.

admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(Usuario)
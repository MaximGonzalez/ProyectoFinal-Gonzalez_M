from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import Q
from blog_app.models import *
from blog_app.forms import *

# Create your views here.


def inicio(request):
    contexto = {'posteos' : Post.objects.all()}
    return render(
        request=request,
        template_name='blog_app/inicio.html',
        context=contexto,
    )



def usuarios(request):
    contexto = {'users': User.objects.all()}
    return render(
        request=request,
        template_name='blog_app/usuarios.html',
        context=contexto,
    )



def posteos(request):
    contexto = {'posteos' :Post.objects.order_by('-fecha_publicacion')}
    return render(
        request=request,
        template_name='blog_app/posteos.html',
        context=contexto,
    )



def comentarios(request):
    contexto = {'comentarios' : Comentario.objects.all()}
    return render(
        request=request,
        template_name='blog_app/comentarios.html',
        context=contexto,
    )



def crear_posteo(request):
    if request.method == 'GET':
        contexto = {'form' : Crear_posteo}
        return render(
        request,
        template_name='blog_app/crear_post.html',
        context=contexto
        )
    else:
        print(request.POST)
        Post.objects.create(titulo = request.POST["titulo"], contenido = request.POST["contenido"])
        contexto = {'form' : Crear_posteo}
        return render(
        request,
        template_name='blog_app/crear_post.html',
        context=contexto
        )



def crear_usuarios(request):
    if request.method == 'GET':
        contexto = {'formulario_usuario' : Crear_usuario}
        return render(
        request,
        template_name='blog_app/crear_usuario.html',
        context=contexto
        )
    else:
        print(request.POST)
        form = Crear_usuario(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            usuario = Usuario(usuario = data["usuario"], contrasenia = data["contrasenia"], mail = data["mail"], nombre = data["nombre"], apellido = data["apellido"], fecha_nacimiento = data['fecha_nacimiento'])
            usuario.save()
            url_exitosa = reverse('usuarios')
        return redirect(url_exitosa)



def crear_posteos(request):
    if request.method == 'GET':
        contexto = {'formulario_post' : Crear_posteo}
        return render(
        request,
        template_name='blog_app/crear_post.html',
        context=contexto
        )
    else:
        print(request.POST)
        formulario = Crear_posteo(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            posteo = Post(titulo = data["titulo"], contenido = data["contenido"], usuario = data["usuario"])
            posteo.save()
            url_exitosa = reverse('inicio')
        return redirect(url_exitosa)



def buscar_posteos(request):
    if request.method == 'POST':
        print(request.POST)
        data = request.POST
        posteos = Post.objects.filter(
            Q(titulo__contains=data['busqueda'].lower())
            | Q(contenido__contains=data['busqueda'].lower())
            )
        if posteos.exists():
            print(posteos)
            contexto = {'posteos' : posteos}
        else:
            print(posteos)
            contexto = {'mensaje': 'No hay resultados'}
        return render(
        request=request,
        template_name='blog_app/buscar_posteos.html',
        context=contexto,
        )



def crear_comentario(request):
    if request.method == 'GET':
        contexto = {'formulario_comentario' : Crear_comentario}
        return render(
        request,
        template_name='blog_app/crear_comentario.html',
        context=contexto
        )
    else:
        print(request.POST)
        formulario = Crear_comentario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            comentario = Comentario(texto = data["texto"])
            comentario.save()
            url_exitosa = reverse('inicio')
        return redirect(url_exitosa)

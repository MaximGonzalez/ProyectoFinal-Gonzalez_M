from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from blog_app.models import Post
from blog_app.forms import Crear_post_form, Crear_comentario_form



# Create your views here.



def inicio(request):
    contexto = {'posteos' : Post.objects.all()}
    return render(
        request=request,
        template_name='blog_app/inicio.html',
        context=contexto,
    )


@login_required
def post(request):
    post = Post.objects.filter(usuario=request.user)
    contexto = {'post':post}
    return render(
        request,
        'blog_app/post.html',
        context=contexto,
    )


@login_required
def crear_post(request):
    if request.method == 'GET':
        return render(
            request, 'blog_app/crear_post.html', {
                'form': Crear_post_form,
            })
    else:
        try:
            print(request.POST)
            form = Crear_post_form(request.POST, request.FILES)
            nuevo_post = form.save(commit=False)
            nuevo_post.usuario = request.user
            nuevo_post.save()
            return redirect('post')
        except ValueError:
            return render(
            request, 'blog_app/crear_post.html', {
                'form': Crear_post_form,
                'error':'Datos invalidos, ingrese nuevamente los datos del post'
            })


@login_required
def post_editar(request, post_id):
    if request.method == 'GET':
        original = get_object_or_404(Post, pk=post_id, usuario=request.user)
        form_edit = Crear_post_form(instance=original)
        return render(request, 'blog_app/post_editar.html', {'original':original, 'form_edit':form_edit})
    else:
        try:
            print(request.POST)
            original = get_object_or_404(Post, pk=post_id, usuario=request.user)
            form_edit = Crear_post_form(request.POST, request.FILES, instance=original)
            form_edit.save()
            return redirect('post')
        except ValueError:
            return render(request, 'blog_app/post_editar.html',
            {'original':original,
            'form_edit' : form_edit,
            'error' : 'Error al actualizar el post'
            })



def post_detalle(request, post_id):
    comentarios = []
    if request.method == 'GET':
        posteo = get_object_or_404(Post, pk=post_id)
        comentarios = posteo.comentario_set.all()
        return render(request, 'blog_app/post_detalle.html', {'posteo':posteo, 'form':Crear_comentario_form, 'comentarios': comentarios})
    else:
        try:
            print(request.POST)
            form = Crear_comentario_form(request.POST)
            nuevo_coment = form.save(commit=False)
            nuevo_coment.autor = request.user
            nuevo_coment.post = Post.objects.get(id=post_id)
            nuevo_coment.save()
            comentarios = posteo.comentario_set.all()
            return render(request, 'blog_app/post_detalle.html', {'posteo':posteo, 'form':Crear_comentario_form, 'comentarios': comentarios})
        except:
            posteo = get_object_or_404(Post, pk=post_id)
            return render(request, 'blog_app/post_detalle.html', {'posteo':posteo, 'form':Crear_comentario_form, 'comentarios': comentarios, 'error':'Error al dejar su comentario'})


def buscar_posteo(request):
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


@login_required
def borrar_post(request, post_id):
    borrar = get_object_or_404(Post, pk=post_id, usuario=request.user)
    if request.method == 'POST':
        borrar.delete()
        return redirect('post')



def about(request):
    return render(
        request=request,
        template_name='blog_app/about.html',
    )
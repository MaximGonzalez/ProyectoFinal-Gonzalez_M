from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from blog_app.models import Post
from blog_app.forms import Crear_post_form

# Create your views here.



def inicio(request):
    contexto = {'posteos' : Post.objects.all()}
    return render(
        request=request,
        template_name='blog_app/inicio.html',
        context=contexto,
    )


@login_required
def usuarios(request):
    contexto = {'users': User.objects.all()}
    return render(
        request=request,
        template_name='blog_app/usuarios.html',
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
            form = Crear_post_form(request.POST)
            nuevo_post = form.save(commit=False)
            nuevo_post.usuario = request.user
            nuevo_post.save()
            return redirect('/')
        except ValueError:
            return render(
            request, 'blog_app/crear_post.html', {
                'form': Crear_post_form,
                'error':'Datos invalidos, ingrese nuevamente los datos del post'
            })



@login_required
def post_detalle(request, post_id):
    if request.method == 'GET':
        detalle = get_object_or_404(Post, pk=post_id, usuario=request.user)
        form_upd = Crear_post_form(instance=detalle)
        return render(request, 'blog_app/post_detalle.html', {'detalle':detalle, 'form_upd' : form_upd})
    else:
        try:
            detalle = get_object_or_404(Post, pk=post_id, usuario=request.user)
            form = Crear_post_form(request.POST, instance=detalle)
            form.save()
            return redirect('post')
        except ValueError:
            return render(request, 'blog_app/post_detalle.html',
            {'detalle':detalle,
            'form_upd' : form_upd,
            'error' : 'Error al actualizar el post'
            })



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



def borrar_post(request, post_id):
    borrar = get_object_or_404(Post, pk=post_id, usuario=request.user)
    if request.method == 'POST':
        borrar.delete()
        return redirect('post')



""" @login_required
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
        return redirect(url_exitosa) """



""" def comentarios(request):
    contexto = {'comentarios' : Comentario.objects.all()}
    return render(
        request=request,
        template_name='blog_app/comentarios.html',
        context=contexto,
    ) """


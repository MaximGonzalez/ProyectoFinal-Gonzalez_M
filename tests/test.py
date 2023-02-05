from django.test import TestCase, Client, RequestFactory
from blog_app.models import *
from django.contrib.auth.models import User
from django.shortcuts import render
from blog_app.models import *
from blog_app.views import *
from login_app.views import *
from blog_app.urls import *
from blog_app.forms import *


##

class PostTestCase(TestCase):
    def setUp(self):
        # Crear un usuario de prueba
        self.user = User.objects.create_user(
            username='testuser', password='password'
        )
        # Crear un post de prueba
        self.post = Post.objects.create(
            titulo='Test Title',
            contenido='Test content',
            usuario=self.user
        )

    def test_post_str(self):
        self.assertEqual(str(self.post), 'Test Title | De: testuser')

    def test_post_titulo(self):
        self.assertEqual(self.post.titulo, 'Test Title')

    def test_post_contenido(self):
        self.assertEqual(self.post.contenido, 'Test content')

    def test_post_fecha_publicacion(self):
        self.assertIsNotNone(self.post.fecha_publicacion)

    def test_post_usuario(self):
        self.assertEqual(self.post.usuario, self.user)

##

class ComentarioTestCase(TestCase):
    def setUp(self):
        # Crear un usuario de prueba
        self.user = User.objects.create_user(
            username='testuser', password='password'
        )
        # Crear un post de prueba
        self.post = Post.objects.create(
            titulo='Test Title',
            contenido='Test content',
            usuario=self.user
        )
        # Crear un comentario de prueba
        self.comentario = Comentario.objects.create(
            post=self.post,
            autor=self.user,
            comentario='Test comment'
        )

    def test_comentario_str(self):
        self.assertEqual(str(self.comentario), f'Comentario por testuser en {self.comentario.fecha_publicacion}: Test comment')

    def test_comentario_post(self):
        self.assertEqual(self.comentario.post, self.post)

    def test_comentario_autor(self):
        self.assertEqual(self.comentario.autor, self.user)

    def test_comentario_comentario(self):
        self.assertEqual(self.comentario.comentario, 'Test comment')

    def test_comentario_fecha_publicacion(self):
        self.assertIsNotNone(self.comentario.fecha_publicacion)

##

class SignupUserTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_signup_user_get(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login_app/signup.html')

    def test_signup_user_post_passwords_dont_match(self):
        response = self.client.post('/signup/', {
            'username': 'testuser',
            'password1': 'password1',
            'password2': 'password2',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login_app/signup.html')
        self.assertContains(response, 'La contrasenia no coincide.')

    def test_signup_user_post_user_already_exists(self):
        User.objects.create_user(username='testuser', password='password')
        response = self.client.post('/signup/', {
            'username': 'testuser',
            'password1': 'password',
            'password2': 'password',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login_app/signup.html')
        self.assertContains(response, 'El usuario ya existe.')

    def test_signup_user_post_success(self):
        response = self.client.post('/signup/', {
            'username': 'testuser',
            'password1': 'password',
            'password2': 'password',
        })
        self.assertRedirects(response, '/')
        self.assertTrue(User.objects.filter(username='testuser').exists())



class InicioViewTestCase(TestCase):
    def setUp(self):
        # Crear un usuario para asociar con los objetos de Post
        self.usuario = User.objects.create_user(username='testuser', password='12345')

        # Crear objetos de Post para utilizar en los test
        self.post1 = Post.objects.create(titulo='Título 1', usuario=self.usuario)
        self.post2 = Post.objects.create(titulo='Título 2', usuario=self.usuario)

        self.factory = RequestFactory()

    def test_inicio_view(self):
        request = self.factory.get('/blog_app/inicio/')
        response = inicio(request)


        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Título 1')
        self.assertContains(response, 'Título 2')



class PostViewTestCase(TestCase):
    def setUp(self):
        # Crear un usuario y un post para utilizar en los test
        self.usuario = User.objects.create_user(username='user1', password='12345')
        self.post = Post.objects.create(
            titulo='Título 1',
            usuario=self.usuario,
        )

        self.factory = RequestFactory()

    def test_post_view(self):
        request = self.factory.get('/blog_app/post/')
        request.user = self.usuario
        response = post(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Título 1')



class PostEditViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.post = Post.objects.create(titulo='Prueba', usuario=self.user)

    def test_post_edit_view(self):
        # Simulamos un usuario autenticado
        self.client.login(username='testuser', password='password')

        # Hacemos una petición GET
        response = self.client.get(reverse('post_editar', args=[self.post.pk]))

        # Verificamos que la respuesta sea correcta
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_app/post_editar.html')
        self.assertContains(response, '<form')
        self.assertIsInstance(response.context['form_edit'], Crear_post_form)

        # Hacemos una petición POST
        data = {'titulo': 'Prueba actualizada', 'contenido': 'Contenido actualizado'}
        response = self.client.post(reverse('post_editar', args=[self.post.pk]), data)

        # Verificamos que se haya actualizado el post y se redirija a la vista de todos los post
        self.post.refresh_from_db()
        self.assertEqual(self.post.titulo, 'Prueba actualizada')
        self.assertEqual(self.post.contenido, 'Contenido actualizado')
        self.assertRedirects(response, reverse('post'))



class PostDetailViewTestCase(TestCase):
    def setUp(self):
        # Crear usuario
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Crear un post
        self.post = Post.objects.create(
            titulo='Test Post',
            contenido='Test Content',
            usuario=self.user
        )

        # Crear un cliente para hacer peticiones
        self.client = Client()


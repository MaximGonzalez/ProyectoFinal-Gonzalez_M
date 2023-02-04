from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from login_app.forms import UserUpdateForm

# Create your views here.


def signup_user(request):
    print(request.POST)
    if request.method == 'GET':
        return render(request, 'login_app/signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('/')
            except IntegrityError:
                return render(request, 'login_app/signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe.',
                })
        else:
            return render(request, 'login_app/signup.html', {
                'form': UserCreationForm,
                'error': 'La contrasenia no coincide.',
            })

@login_required
def signout_user(request):
    logout(request)
    return redirect('/')


def signin_user(request):
    print(request.POST)
    if request.method == 'GET':
        return render(request, 'login_app/signin.html', {
            'form': AuthenticationForm,
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login_app/signin.html', {
            'form': AuthenticationForm,
            'error':'El usuario o la contrasenia son incorrectos'
            })
        else:
            login(request, user)
            return redirect('/')



class ProfileEditView(LoginRequiredMixin, UpdateView):
    model_class = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('inicio')
    template_name = 'login_app/usuario.html'

    def get_object(self, queryset=None):
        return self.request.user
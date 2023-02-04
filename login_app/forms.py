from django.forms import ModelForm
from blog_app.models import Post, Comentario
from django.contrib.auth.models import User
from django import forms



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
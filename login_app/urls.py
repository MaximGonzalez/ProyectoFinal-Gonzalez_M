from django.contrib import admin, staticfiles
from django.urls import path, include
from .views import *

urlpatterns = [
    path("signup/", signup_user, name="signup_user"),
    path("logout/", signout_user, name="signout_user"),
    path("signin/", signin_user, name="signin_user"),
    #path('blog_app', include('blog_app.urls')),
]
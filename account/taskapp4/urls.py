from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("signup",views.register,name="signup"),
    path("signin",views.login,name="login"),
    path("logged",views.logged,name="logged"),
]
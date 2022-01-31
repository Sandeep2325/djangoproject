from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path("",views.personel),
    path("infoo",views.infoo ,name="infoo"),
]
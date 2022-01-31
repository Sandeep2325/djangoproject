from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.home),
    path("city",views.city)]


"""path("bengaluru",views.bengalore),
    path("chennai",views.chennai),
    """

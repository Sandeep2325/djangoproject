from django.urls import path
from . import views

app_name = "apptask21"   


urlpatterns = [
    #path("", views.homepage, name="homepage"),
    path("",views.dummy),
    path("upload", views.upload, name="upload")
]
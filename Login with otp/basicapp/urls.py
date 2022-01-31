from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	path("",views.home,name="home"),
    path("",views.home,name="home"),
    #path("send_otp",views.send_otp,name="send_otp")
    path("send_otp_",views.send_otp_,name="send_otp_"),
    path("success",views.success,name="success"),
    ]
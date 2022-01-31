from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	#path("",views.home,name="home"),
    path("",views.home,name="home"),
    path("send_otp",views.send_otp,name="send otp"),
    path("otp2",views.otp2,name="otp2"),
    path("otp",views.success,name="otp"),]
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random
def generateOTP() :
    digits = "0123456789"
    OTP = ""
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

def send_otp(request):
    email=request.GET.get("email")
    o=generateOTP()
    print(o)
    print(email)
    htmlgen = '<p>Your OTP is <strong>'+o+'</strong></p>'
    send_mail('OTP request',o,'<gmail id>',[email],fail_silently=False,html_message=htmlgen)
    return HttpResponse(o)

def home(request):
    email=request.GET.get("email")
    global o
    o=generateOTP()
    print(o)
    print(email)
    htmlgen = '<p>Your OTP is <strong>'+o+'</strong></p>'
    send_mail('OTP request',o,'<gmail id>',[email],fail_silently=False,html_message=htmlgen)
    return render(request,"verify/home2.html")
    
def otp2(request):
    email=request.GET.get("email")
    print(email)
    return render(request,"verify/otpp.html")

    """otp1=request.GET.get("otp1")
    if o==otp1:
        return HttpResponse("otp verified")
    else:
        return HttpResponse("invalid otp")"""
def success(request):
    otp1=request.GET.get("otp1")
    print(otp1)
    if o==otp1:
        return HttpResponse("otp verified")
    else:
        return HttpResponse("invalid otp")
    

    
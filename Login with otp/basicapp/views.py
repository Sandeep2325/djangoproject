from django.shortcuts import render,redirect
from django.http import HttpResponse
from basic import settings
from django.core.mail import send_mail
import math, random
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random
"""def generateOTP() :
    digits = "0123456789"
    OTP = ""
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

def send_otp(request):
    if request.method=="POST":
        email=request.POST.get("email")
        print(email)
        o=generateOTP()
        #htmlgen = '<p>Your OTP is <strong>'+o+'</strong></p>'
        send_mail('Hi,your One Time Password is ',o,'gowdasandeep8105@gmail.com',[email],fail_silently=False,)
        #send_mail('OTP request',o,'<gmail id>',[email],fail_silently=False,html_message=htmlgen)
        return HttpResponse(o)

def home(request):
    return render(request, "home.html")"""
#__________________________________________________________________________________without AJAX_____________________________________________________________________________________
def home(request):
    return render(request, "index.html")
def generateOTP() :
    digits = "A12B34C5627859D"
    OTP = ""
    for i in range(5) :
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

def send_otp_(request):
    if 'form1':          
        if request.method=="POST":
            global email
            email=request.POST.get("email")
            global otp
            otp=generateOTP()
            print(otp)
            print(email)
            send_mail('Hi,your One Time Password is ',otp,'gowdasandeep8105@gmail.com',[email],fail_silently=False,)
            #email1=email
            print("++++++++++++++++++++++++++++++++++++++email sent+++++++++++++++++++++++++++++++++++")
            return render (request,"otp.html")
    #print(email)
    if 'form2':
        if request.method=="POST":
            email=request.POST.get("email")
            #global otp
            otp=generateOTP()
            print(otp)
            #print(email)
            send_mail('Hi,your One Time Password is(resent) ',otp,'gowdasandeep8105@gmail.com',[email],fail_silently=False,)
        return redirect("send_otp_")

def success(request):
    otp2=request.POST.get("otp")
    print("______________________________________________________________",otp)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",otp2)
    if otp==otp2:
        return render (request,"signed.html")
    else:
        return render (request,"invalid.html")

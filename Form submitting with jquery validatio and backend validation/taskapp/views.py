from django.shortcuts import render
from django.http import HttpResponse
from .forms import profileForm
from django.views import View
from .models import Info
from django.db import models

def personel(request):
    return render(request,"taskapp/index.html")

def infoo(request):
   if request.method=='POST':
       form=profileForm(request.method=='POST' or None)
       if form.is_valid():
            firstname=request.POST.get('firstname')
            lastname=request.POST.get('lastname')
            dob=request.POST.get('dob')
            Relationship=request.POST.get('Relationship')
            gender=request.POST.get('gender')
            lang=request.POST.get('lang')

            hobbies=request.POST.get('hobbies')
            picture=request.POST.get('picture')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            door=request.POST.get('door')
            street=request.POST.get('street')

            city=request.POST.get('city')
            dist=request.POST.get('dist')
            state=request.POST.get('state')
            country=request.POST.get('country')
            code=request.POST.get('code')
            course=request.POST.get('course')

            institute=request.POST.get('institute')
            address=request.POST.get('address')
            started=request.POST.get('started')
            passed=request.POST.get('passed')
            gpa=request.POST.get('gpa')
            resume=request.POST.get('resume')
            password=request.POST.get('password')
            confirm_password=request.POST.get('confirm_password')
            #print(gpa,passed)
            data=Info(firstname=firstname,lastname=lastname,dob=dob,Relationship=Relationship,gender=gender,
            lang=lang,hobbies=hobbies,picture=picture,email=email,phone=phone,door=door,street=street,
            city=city,dist=dist,state=state,country=country,code=code,course=course,institute=institute,
            address=address,started=started,passed=passed,gpa=gpa,resume=resume,password=password,confirm_password=confirm_password)
            data.save()
            print(data)
            return render(request,"taskapp/index.html")
        #success="user"+firstname,lastname+"data submitted"

        #return HttpResponse(success)

         


 


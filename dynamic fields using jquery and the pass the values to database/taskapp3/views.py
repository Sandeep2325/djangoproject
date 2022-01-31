from django.shortcuts import render
from django.http import HttpResponse
from .models import fields

def dynamic(request):
    return render(request,"taskapp3/index.html")
def upload(request):
    if request.method == 'POST':
        fullnames=request.POST.getlist("fullname[]")
        hobbiess=request.POST.getlist("hobbies[]")
        dictionary=dict(zip(fullnames,hobbiess))
        print(dictionary)
        for fullname, hobbies in dictionary.items():
            data=fields(fullname=fullname,hobbies=hobbies)
            data.save()
    return render(request,"taskapp3/index.html")
   



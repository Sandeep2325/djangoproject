from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"user/index.html")
def logged(request):
    return render(request,"user/loggedin.html")
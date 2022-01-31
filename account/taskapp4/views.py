from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home(request):
    
    return render(request,"taskapp4/index.html")
def register(request):
    
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        print(first_name,last_name,username,email,password1)
        if password1==password2:
            if User.objects.filter(username=username).exists():
                print("----------------------------------------------------user name taken")
                messages.info(request,'username taken')
            elif User.objects.filter(email=email).exists():
                print("email taken----------------------------------------------------")
                messages.info(request,"email taken")
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                
                print("--------------------------------------------------------------------user created",user)
                return redirect("login")
        else:
            messages.info(request,"password not matched")
            print("_____________________________________________passwords not matched")
            return redirect("signup")
        return redirect("signup")
        
    return render(request,"taskapp4/signup.html")
def login(request):
    if request.method=="POST":
        username=request.POST.get('username', False)
        email=request.POST['email']
        password=request.POST['password']
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",username,email,password)
        user=auth.authenticate(username=username,password=password,email=email)
        
        print("+++++++++++++++++++++++++++++++authenticated",user)

        #auth.login(request,user)
        #print("okkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
        #return redirect("/")

        if user is not None:
            auth.login(request,user)
            return redirect("logged")
        else:
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++invalid creditials")
            messages.info(request,'invalid creditials')
            return redirect("login")
    else:
        return render(request,"taskapp4/signin.html")

def logged(request):
    return render (request,"taskapp4/loggedin.html")
    
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
def home(request):
    return render(request,"taskapp4/home.html")
def signup(request):
	if request.method == "POST":
		print("+++++++++++++++++++++++++++++++++++++method is post")
		form = NewUserForm(request.POST)
		if form.is_valid():
			print("++++++++++++++++++++++++++++++++++++++++++++form is valid")
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("signup")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="taskapp4/signup.html", context={"register_form":form})
def signin(request):
	if request.method == "POST":
		form = AuthenticationForm(request,data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			print("##################################################",password)
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged")
				return redirect("taskapp4:home")
			else:
				print("___________________________________________________________failed")
				messages.error(request,"Invalid username or password.")
		else:
			print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++failed")
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="taskapp4/signin.html", context={"login_form":form})
def loggedin(request):
    return render(request,"taskapp4/loggedin.html")

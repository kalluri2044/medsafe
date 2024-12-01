from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"you are now loggedin")
            return redirect("dashboard")
        else:
            messages.error(request,"Invalid credentials")
            return redirect("login")
    else:
        return render(request,"accounts/login.html")
    
def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request,"you are now loggedout")
        return redirect("index")
    
def register(request):
    if request.method == "POST":
        full_name = request.POST["fullName"]
        phone_number = request.POST["phoneNumber"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["confirmPassword"]
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"username already exist")
                return redirect("register")
            else:
                user = User.objects.create_user(first_name=full_name,username=username,email=email,password=password)
                user.save()
                messages.success(request,"you are now register you can login")
                return redirect("login")
        else:
            messages.error(request,"password donot match")
            return redirect("register")
    else:
        return render(request,"accounts/register.html")

def dashboard(request):
    return HttpResponse("Dashboard data")


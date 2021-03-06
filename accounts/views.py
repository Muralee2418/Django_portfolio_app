from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect("/")
def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        print("username is"+user.username)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid Credential")
            return redirect("login")
    else:
        return render(request,"login.html")
def register(request):

    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        confirm=request.POST["password_confirm"]
        if password==confirm:
            if User.objects.filter(username=username).exists():
                messages.info(request,"User already exist")
                return redirect("register")
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()  
        else:
            messages.info(request,"password doesn't match")
            return redirect("register")
        return redirect("login")

    else:
        return render(request,"register.html")
    
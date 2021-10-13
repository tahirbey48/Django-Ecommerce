from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from users.forms import LoginForm, RegisterForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.
def loginfun(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username,password = password)
        if user is None:
            messages.info(request,"Wrong username or password!")
            return render(request,"login.html", {"form": form})

        messages.success(request,"Login successful")
        login(request,user)
        return redirect("app1:home")
    return render(request,"login.html",{"form": form})



def logoutfun(request):
    logout(request)
    messages.success(request,"Logout Successful.")
    return redirect("app1:home")


def registerfun(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")

        newUser = User(username =username, email = email)
        newUser.set_password(password)
        newUser.save()
        messages.info(request,"Başarıyla Kayıt Oldunuz...")
        return redirect("users:login")
    return render(request,"register.html", {"form" : form})
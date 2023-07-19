from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app.models import CustomUser
from django.views.decorators.cache import never_cache


def index(request):
    return render(request, 'index.html')

@never_cache
def handlesignup(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("pass1")
        confirmpassword = request.POST.get("pass2")

        if password != confirmpassword:
            messages.warning(request, "Passwords do not match")
            return redirect('/signup')

        if CustomUser.objects.filter(username=uname).exists():
            messages.info(request, "Username is taken")
            return redirect('/signup')

        if CustomUser.objects.filter(email=email).exists():
            messages.info(request, "Email is taken")
            return redirect('/signup')

        myuser = CustomUser(username=uname, email=email)
        myuser.set_password(password)
        myuser.save()
        messages.success(request, "Signup successful. Please login!")
        return redirect('/login')

    return render(request, 'signup.html')

@never_cache
def handlelogin(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pass1 = request.POST.get("pass1")
        myuser = authenticate(username=uname, password=pass1)

        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login successful")
            return redirect('/home')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('/login')

    return render(request, 'login.html')
@never_cache
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('/login')
@never_cache
def handlelogout(request):
    logout(request)
    messages.info(request, "Logout successful")
    return redirect('/login')

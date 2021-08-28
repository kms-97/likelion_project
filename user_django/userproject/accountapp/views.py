from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def main(request):
    return render(request, "main.html")

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request = request, username = username, password = password)
            if user is not None :
                login(request, user)
            return redirect("main")
    else:
        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect("main")

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("main")
    else:
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, "signup.html", context)

        
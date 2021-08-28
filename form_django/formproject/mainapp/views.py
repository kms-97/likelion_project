from django.shortcuts import render, redirect
from django import forms
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from .models import *
from .forms import *

# Create your views here.
def main(request):
    blogs = Blog.objects.all()
    context = {
        'blogs' : blogs,
    }
    return render(request, 'main.html', context)

def create_page(request):
    forms = BlogForm()
    context = {
        'forms' : forms,
    }
    return render(request, 'create.html', context)

def create(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.pub_date = timezone.now()
        new_blog.save()
    return redirect('main')


#
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid(): #유효성 검사
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username = username, password=password)
            if user is not None :
                login(request, user)
            return redirect("main")
        else:
            return redirect('main')
    else :
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form}) #Get방식

def logout_view(requset):
    logout(requset)
    return redirect("main")

def signup_view(request):
    if request.method == "POST": #요청방식이 POST
        form = RegisterForm(request.POST)
        if form.is_valid(): #form 유효성 검사
            user = form.save()
            login(request, user)
        return redirect("main")
    else: #요청방식이 GET
        form = RegisterForm()
    return render(request, 'signup.html', {'form':form})
from django.shortcuts import redirect, render, get_object_or_404
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .models import Blog, Comment
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages
import datetime
from django.utils import timezone

from django.core.paginator import Paginator

def main(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'blogs' : blogs,
        'posts' : posts,
    }
    return render(request, 'main.html', context)

def detail(request, id):
    detail_data = get_object_or_404(Blog, pk=id)
    comments = Comment.objects.filter(blog_id = id)
    context = {
        'title' : detail_data.title,
        'writer' : detail_data.writer,
        'body' : detail_data.body,
        'pub_date' : detail_data.pub_date,
        'id' : id,
        'comments':comments,
        'image':detail_data.image,
    }
    return render(request, 'detail.html', context)

def create_page(request):
    return render(request, 'create.html')

def create(request):
    new_data = Blog()
    new_data.title = request.POST['title']
    new_data.writer = request.POST['writer']
    new_data.body = request.POST['body']
    if 'image' in request.FILES:
        new_data.image = request.FILES['image']
    new_data.pub_date = timezone.now()
    new_data.save()
    return redirect('main')

def update_page(request, id):
    update_data = get_object_or_404(Blog, pk=id)
    context = {
        'id' : id,
        'title' : update_data.title,
        'writer' : update_data.writer,
        'body' : update_data.body,
        'image' : update_data.image,
    }
    return render(request, 'update.html', context)

def update(request, id):
    update_data = get_object_or_404(Blog, pk=id)
    update_data.title = request.POST['title']
    update_data.writer = request.POST['writer']
    update_data.body = request.POST['body']
    update_data.pub_date = timezone.now()
    update_data.image = request.FILES['image']
    update_data.save()
    return redirect('main')

def delete(request, id):
    delete_data = get_object_or_404(Blog, pk=id)
    delete_data.delete()
    return redirect('main')


def create_comment(request, id):
    new_comment = Comment()
    blog_id = Blog.objects.get(pk=id)
    new_comment.blog_id = blog_id
    new_comment.user = request.POST['user']
    new_comment.content = request.POST['content']
    new_comment.pub_date = timezone.now()
    new_comment.save()

    return redirect('detail', id)

def delete_comment(request,id,comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()

    return redirect('detail',id)


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid(): #????????? ??????
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username = username, password=password)
            if user is not None :
                login(request, user)
                return redirect('main')
            else:
                last_messages = messages.get_messages(request)
                last_messages.used = True
                messages.info(request, '??????????')
                return redirect("login")
        else:
            last_messages = messages.get_messages(request)
            last_messages.used = True
            messages.info(request, '????????? ??????')
            return redirect("login")
    else :
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form}) #Get??????


def logout_view(request):
    logout(request)
    return redirect("main")

def signup_view(request):
    if request.method == "POST": #??????????????? POST
        form = UserCreationForm(request.POST)
        if form.is_valid(): #form ????????? ??????
            user = form.save()
            login(request, user)
            return redirect("main")
        else:
            last_messages = messages.get_messages(request)
            last_messages.used = True
            messages.info(request, '???????????? ?????????')
            return redirect("signup")
    else: #??????????????? GET
        form = UserCreationForm()
        return render(request, 'signup.html', {'form':form})
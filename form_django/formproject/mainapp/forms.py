from django import forms
from django.db.models import fields
from django.db.models.base import Model
from django.forms import utils
from .models import *

from django.contrib.auth.forms import UserCreationForm


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'writter', 'body', 'image']

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'nickname', 'university', 'location']
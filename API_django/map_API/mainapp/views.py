from django.shortcuts import render
from .models import *

# Create your views here.

def main(request):
    cafes = cafe.objects.all()
    context = {
        'cafes' : cafes,
    }
    return render(request, 'main.html', context)
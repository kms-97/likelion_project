from django.shortcuts import render, get_object_or_404, redirect
from .models import Teammate
# Create your views here.

def main(request):
    teammates = Teammate.objects.all()
    context = {
        'teammates' : teammates,
    }
    return render(request, 'main.html', context)

def detail(request, id):
    detail.data = get_object_or_404(Teammate, pk=id)
    context = {
        'name' : detail.data.name,
        'birth' : detail.data.birth,
        'live' : detail.data.live,
        'birthlocation' : detail.data.birthlocation,
        'haslover' : detail.data.haslover,
        'food' : detail.data.food,
        'major' : detail.data.major,
        'dream' : detail.data.dream,
        'alchol' : detail.data.alchol,
        'number' : detail.data.number,
        'id' : id,
    }
    return render(request, 'detail.html', context)

def create_page(request):
    return render(request, 'create_page.html')

def create(request):
    new_data = Teammate()
    new_data.name = request.POST['name']
    new_data.birth = request.POST['birth']
    new_data.birthlocation = request.POST['birthlocation']
    new_data.live = request.POST['live']
    new_data.major = request.POST['major']
    new_data.number = request.POST['number']
    new_data.food = request.POST['food']
    new_data.haslover = request.POST['haslover']
    new_data.alchol = request.POST['alchol']
    new_data.dream = request.POST['dream']
    new_data.save()
    return redirect('main')

def update_page(request, id):
    update_data = get_object_or_404(Teammate, pk=id)
    context = {
        'id' : id,
        'update_data' : update_data,
    }
    return render(request, 'update_page.html', context)

def update(request, id):
    update_data = get_object_or_404(Teammate, pk=id)
    update_data.name = request.POST['name']
    update_data.birth = request.POST['birth']
    update_data.birthlocation = request.POST['birthlocation']
    update_data.live = request.POST['live']
    update_data.major = request.POST['major']
    update_data.number = request.POST['number']
    update_data.food = request.POST['food']
    update_data.haslover = request.POST['haslover']
    update_data.alchol = request.POST['alchol']
    update_data.dream = request.POST['dream']
    update_data.save()
    return redirect('main')

def delete(request, id):
    delete_data = get_object_or_404(Teammate, pk=id)
    delete_data.delete()
    return redirect('main')

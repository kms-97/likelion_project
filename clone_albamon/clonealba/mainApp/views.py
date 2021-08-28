from django.shortcuts import render, get_object_or_404, redirect
from .models import notice, comment
from django.utils import timezone

# Create your views here.

def main(request):
    Notice = notice.objects.all()
    context = {
        'notice': Notice,
    }
    return render(request, 'main.html', context)

def detail (request, id):
    Detail = get_object_or_404(notice, pk=id)
    comments = comment.objects.filter(notice_id = id)
    context = {
        'detail': Detail,
        'image': Detail.image,
        'id': id,
        'comment': comments,
    }
    return render(request, 'detail.html', context)

def registerPage (request):
    return render(request, 'register.html')

def register (request):
    new_data = notice()
    new_data.company = request.POST['company']
    new_data.where = request.POST['where']
    if request.POST['period'] != '':
        new_data.period = request.POST['period']
    else:
        new_data.period = None
    new_data.day = request.POST['day']
    if 'time' in request.POST:
        new_data.time = request.POST['time']
    if request.POST['pay'] != '':
        new_data.pay= request.POST['pay']
    else:
        new_data.pay = None
    new_data.detail = request.POST['detail']
    if request.POST['image'] != '':
        new_data.image = request.FILES['image']
    new_data.valunteer = 0
    new_data.save()
    return redirect('main')

def delete (request, id):
    delete_data = get_object_or_404(notice, pk=id)
    delete_data.delete()
    return redirect('main')

def update_page(request, id):
    update_data = get_object_or_404(notice, pk=id)
    context = {
        'id' : id,
        'update_data' : update_data,
        'image' : update_data.image,
    }
    return render(request, 'updatePage.html', context)

def update(request, id):
    update_data = get_object_or_404(notice, pk=id)
    update_data.company = request.POST['company']
    update_data.where = request.POST['where']
    if request.POST['period'] != '':
        update_data.period = request.POST['period']
    else:
        update_data.period = None
    update_data.day = request.POST['day']
    if 'time' in request.POST:
        update_data.time = request.POST['time']
    if request.POST['pay'] != '':
        update_data.pay = request.POST['pay']
    else:
        update_data.pay = None
    update_data.detail = request.POST['detail']
    if 'image' in request.FILES:
        update_data.image = request.FILES['image']
    update_data.save()
    return redirect('detail', id)

def apply(request, id):
    apply = get_object_or_404(notice, pk=id)
    apply.valunteer += 1
    apply.save()
    return redirect('detail', id)

def cancel(request, id):
    apply = get_object_or_404(notice, pk=id)
    apply.valunteer -= 1
    apply.save()
    return redirect('detail', id)

def newComment(request, id):
    new_data = comment()
    notice_id = notice.objects.get(pk=id)
    new_data.notice_id = notice_id
    new_data.writter = request.POST['writter']
    new_data.body = request.POST['body']
    new_data.date = timezone.now()
    new_data.save()
    return redirect('detail', id)

def deleteComment(request, id, comment_id):
    delete_data = get_object_or_404(comment, pk=comment_id)
    delete_data.delete()
    return redirect('detail', id)

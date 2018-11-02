from django.shortcuts import render, reverse
from .models import DayOff
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
     return render(request, 'shifty/index.html', {

     })

def index2(request):
     return render(request, 'shifty/index2.html', {

     })

def get_days_off(request):
    days_off = DayOff.objects.all()
    output = []
    for day_off in days_off:
        output.append(day_off.to_dict())
    print(output)
    return JsonResponse({'events': output})

def save_day_off(request):
    data = json.loads(request.body)
    print(data)
    title = data['title']
    start_date = datetime.datetime.strptime(data['start_date'], '%m/%d/%Y')
    end_date = datetime.datetime.strptime(data['end_date'], '%m/%d/%Y')
    user_item = DayOff(name=title, start=start_date, end=end_date)
    user_item.save()
    return HttpResponse('ok')



@login_required
def index(request):
    print(request.user.username)
    return render(request, 'shifty/index.html', {})


def register_user(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    login(request, user)
    return HttpResponseRedirect(reverse('shifty:index'))


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('shifty:index'))
    return HttpResponseRedirect(reverse('shifty:register'))


def register(request):
    return render(request, 'shifty/register.html', {})


def logout_user(request):
    logout(request)
    return render(request, 'shifty/register.html', {})

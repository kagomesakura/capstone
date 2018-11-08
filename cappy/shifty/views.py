from django.shortcuts import render, reverse
from .models import DayOff
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def signin(request):
     return render(request, 'shifty/signin.html', {})

@login_required
def calendar(request):
     return render(request, 'shifty/calendar.html', {})

@login_required
def get_days_off(request):
    days_off = DayOff.objects.all()
    output = []
    for day_off in days_off:
        output.append(day_off.to_dict())
    print(output)
    return JsonResponse({'events': output})

@login_required
def save_day_off(request):
    data = json.loads(request.body)
    start_date = datetime.datetime.strptime(data['start_date'], '%b/%d/%y')
    end_date = datetime.datetime.strptime(data['end_date'], '%b/%d/%y')
    user_item = DayOff(user=request.user, start=start_date, end=end_date, all_day=False)
    user_item.save()
    return HttpResponse('ok')



def index(request):
    return render(request, 'shifty/signin.html', {})


def register_user(request):
    try:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        login(request, user)
        return HttpResponseRedirect(reverse('shifty:calendar'))
    except ValueError:
        return HttpResponseRedirect(reverse('shifty:signin'))



def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('shifty:calendar'))
    return HttpResponseRedirect(reverse('shifty:signin'))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('shifty:signin'))

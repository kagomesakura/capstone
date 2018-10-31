from django.shortcuts import render
from .models import DayOff
from django.http import HttpResponse, JsonResponse
import json
import datetime
from django.contrib.auth import authenticate, login, logout


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

def mylogin(request):
    # retrieve the variables from the form submission
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # redirect to index.html
    else:
        # return 'invalid login' error message

        def logout_view(request):
            logout(request)
            # redirect to login page (refresh?)

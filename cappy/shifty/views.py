from django.shortcuts import render
from .models import DayOff
from django.http import HttpResponse, JsonResponse
import json


def index(request):
     return render(request, 'shifty/index.html', {})



def get_days_off(request):
    days_off = DayOff.objects.all()
    output = []
    for day_off in days_off:
        output.append(day_off.to_dict())
    return JsonResponse({'days_off': days_off})

def save_day_off(request):
    data = json.loads(request.body)
    print(data)
    title = data['title']
    start_date = data['start_date']
    end_date = data['end_date']
    user_item = DayOff(text=title)
    user_item.save()
    return HttpResponse('TEST')



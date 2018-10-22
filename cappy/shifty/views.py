from django.shortcuts import render
#from .models import userDay, userName, userTime

# Create your views here.
def index(request):
     return render(request, 'shifty/index.html', {})




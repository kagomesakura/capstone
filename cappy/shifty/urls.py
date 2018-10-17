from django.urls import path
from . import views

app_name = 'shifty'
urlpatterns = [
    path('', views.index, name='index'),
]
from django.urls import path
from . import views


app_name = 'shifty'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_days_off/', views.get_days_off, name='get_days_off'),
    path('save_day_off/', views.save_day_off, name='save_day_off'),
]

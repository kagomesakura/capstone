from django.urls import path, include
from . import views


app_name = 'shifty'
urlpatterns = [
    path('', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('get_days_off/', views.get_days_off, name='get_days_off'),
    path('save_day_off/', views.save_day_off, name='save_day_off'),
    path('accounts/', include('django.contrib.auth.urls')),
]
from django.urls import path, include
from . import views


app_name = 'shifty'
urlpatterns = [
    path('', views.index, name='signin'),
    path('register_user/', views.register_user, name='register_user'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('todo/', views.todo, name='todo'),
    path('calendar/', views.calendar, name='calendar'),
    path('get_days_off/', views.get_days_off, name='get_days_off'),
    path('save_day_off/', views.save_day_off, name='save_day_off'),
    # path('accounts/', include('django.contrib.auth.urls')),
]




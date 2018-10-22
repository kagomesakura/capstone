from django.urls import path
from . import views


app_name = 'shifty'
urlpatterns = [
    path('', views.index, name='index'),
    # path('addtext/', views.addtext, name='addtext'),
    # path('gettext/', views.gettext, name='gettext')
]
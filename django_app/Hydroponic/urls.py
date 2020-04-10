# -*- coding: utf-8 -*-

from django.urls import path
from .import views
from .views import plotGraph, temperature, humidity, picture, grow, setting

urlpatterns = [
    path('', views.index, name='index'),
    path('Log/temperature', temperature.as_view(), name='temperatureLog'),
    path('Log/humidity', humidity.as_view(), name='humidityLog'),
    path('Log/picture', picture.as_view(), name='pictureLog'),
    path('Log/grow', grow.as_view(), name='growLog'),
    path('Setting', setting.as_view(), name='setting'),

    path('plot', plotGraph.as_view(), name='plot'),

    path('reboot', views.rebootCmd, name='reboot'),
    ]
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 21:32:53 2020

@author: kobayashitakumi
"""
from django.urls import path
from . import views
# from .views import HelloView

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
    path('find', views.find, name='find'),
]
# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.home, name = 'home-testing'),
    
    
    path('withdraw/', views.withdraw, name='withdraw'),
    path('deposit/', views.deposit, name='deposit'),
    path('transfer/', views.transfer, name='transfer'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]

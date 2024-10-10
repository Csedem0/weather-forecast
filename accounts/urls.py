from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather_forecast, name='weather_forecast'),
    path('map/', views.map, name='map'),
    path('contactus/', views.contactus, name='contactus'),
    path('aboutus/', views.aboutus, name='aboutus'),
]


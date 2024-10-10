from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather_forecast, name='weather_forecast'),
]


# weather/admin.py

from django.contrib import admin
from .models import City  # Import the City model

@admin.register(City)  # Registering City model
class CityAdmin(admin.ModelAdmin):
    list_display = ['name']

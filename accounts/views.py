import requests
from django.shortcuts import render
from .forms import CityForm

API_KEY = '141710af2113bab9f55ef73e1bcd33d5'  # Replace with your actual API key

def weather_forecast(request):
    weather_data = None
    error_message = None

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(api_url)

            if response.status_code == 200:
                weather_data = response.json()
            else:
                error_message = "City invalid or not found."
    else:
        form = CityForm()

    return render(request, 'weather/weather.html', {'form': form, 'weather_data': weather_data, 'error_message': error_message})

def map(request):
    return render(request, 'weather/map.html')

def aboutus(request):
    return render(request, 'weather/aboutus.html')

def contactus(request):
    return render(request, 'weather/contactus.html')
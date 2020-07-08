from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    cities = City.objects.all() #return all the cities in the database

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=533f3c2b6dff8ef06f261a332fd8c6d7'
    url1 = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=new delhi&units=imperial&cnt=7&appid=533f3c2b6dff8ef06f261a332fd8c6d7'

    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate

    form = CityForm()

    weather_data = []
    forecast_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
        daily_forecast = requests.get(url1.format(city)).json()

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
        for item in daily_forecast['list']:
            forecast = {
                'icons' : item['weather'][0]['description'],
            }

        weather_data.append(weather) #add the data for the current city into our list

        forecast_data.append(forecast)

    context = {'weather_data' : weather_data, 'form' : form, 'forecast' : forecast_data}

    return render(request, 'weather/index.html', context) #returns the index.html template
import requests
from django.shortcuts import render

def index(request):
    context = {}
    if request.method == 'POST':
        city = request.POST['city']
        api_key = 'b5db745fc6ca377cb941d63f4ce9e8f4'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:  # Check if the request was successful
            weather_data = response.json()
            print(weather_data)
            if 'main' in weather_data:
                
                context = {
                    'city': city, 
                    'temperature': weather_data['main']['temp'],
                    'description': weather_data['weather'][0]['description'],
                    'icon': weather_data['weather'][0]['icon'],
                }
            else:
                context = {'error': 'Weather data not available for this city.'}
        else:
            context = {'error': 'Failed to retrieve weather data. Please check the city name.'}

 
    return render(request, 'weather/index.html', context)

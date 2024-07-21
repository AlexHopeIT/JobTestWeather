import requests
from JobTest.settings import API_KEY


def get_weather(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get('https://api.openweathermap.org/data/2.5/weather',
                            params=params)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'city': city_name,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        return weather_data
    else:
        return None

from django.shortcuts import render

from .forms import CityForm
from .api_client import get_weather


def index(request):
    weather_data = None
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['city_name']
            weather_data = get_weather(city_name)
    else:
        form = CityForm()
    return render(request, 'weather/index.html', {'form': form,
                                                  'weather_data': weather_data})


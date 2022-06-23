# Geocoding API URL: 'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={app_id}'
# Weather API URL: https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={
# API key}


import requests

app_id = '705a6037e30f23562ca8c60af844f92e'
city = input().lower()
URL = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={app_id}'
unit = "metric"

try:
    r = requests.get(url=URL)

    lat = r.json()[1]['lat']
    lon = r.json()[1]['lon']

    WEATHER_URL = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={app_id}&units={unit}'

    weather = requests.get(url=WEATHER_URL)

    print(weather.json()['weather'][0]['main'])
    print("Temperature: ", weather.json()['main']['temp'], "°C")
    print("Feels like: ", weather.json()['main']['feels_like'], "°C")
except IndexError:
    print("Sorry, that is either not a city or is an unsupported city :(")

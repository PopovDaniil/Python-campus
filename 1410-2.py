import requests

city = input('Введите город:')
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': 'ff804351b97f7a93823cbf829df18b62'})
data = res.json()
print("conditions:", data['weather'][0]['description'])
print("temp:", data['main']['temp'])
print("temp_min:", data['main']['temp_min'])
print("temp_max:", data['main']['temp_max'])

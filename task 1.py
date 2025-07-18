import requests
import matplotlib.pyplot as plt

# 🔑 Replace this with your own OpenWeatherMap API key
API_KEY = 'your_api_key_here'

# List of cities to fetch weather data
cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata']

# API endpoint
base_url = 'http://api.openweathermap.org/data/2.5/weather'

# Lists for data
temperatures = []
humidities = []
pressures = []

# Fetch and collect data
for city in cities:
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    res = requests.get(base_url, params=params)
    data = res.json()
    
    if res.status_code == 200:
        temperatures.append(data['main']['temp'])
        humidities.append(data['main']['humidity'])
        pressures.append(data['main']['pressure'])
    else:
        print(f"Failed to get data for {city}")
        temperatures.append(0)
        humidities.append(0)
        pressures.append(0)

# 📊 Plotting
plt.figure(figsize=(14, 6))

# Temperature
plt.subplot(1, 3, 1)
plt.bar(cities, temperatures, color='orange')
plt.title('Temperature (°C)')
plt.ylabel('°C')

# Humidity
plt.subplot(1, 3, 2)
plt.bar(cities, humidities, color='skyblue')
plt.title('Humidity (%)')
plt.ylabel('%')

# Pressure
plt.subplot(1, 3, 3)
plt.bar(cities, pressures, color='green')
plt.title('Pressure (hPa)')
plt.ylabel('hPa')

plt.suptitle("Weather Data Visualization - OpenWeatherMap", fontsize=16)
plt.tight_layout()
plt.show()

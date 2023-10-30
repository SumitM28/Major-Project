# # # import requests
# # # import geocoder

# # # # Replace 'YOUR_OPENWEATHERMAP_API_KEY' with your OpenWeatherMap API key
# # # openweathermap_api_key = 'Y46b1f792696849e1a237f5c8a2b1d79e'

# # # def get_current_weather(api_key, lat, lon):
# # #     weather_api_url = f'http://api.openweathermap.org/data/2.5/weather'
# # #     params = {
# # #         'lat': lat,
# # #         'lon': lon,
# # #         'appid': api_key,
# # #         'units': 'metric'  # You can change this to 'imperial' for Fahrenheit
# # #     }

# # #     try:
# # #         response = requests.get(weather_api_url, params=params)
# # #         data = response.json()
# # #         weather_description = data['weather'][0]['description']
# # #         temperature = data['main']['temp']
# # #         location = data['name']
# # #         print(f"Weather in {location}: {weather_description}")
# # #         print(f"Temperature: {temperature}°C")
# # #     except Exception as e:
# # #         print(f"Error getting weather data: {e}")

# # # def get_location():
# # #     try:
# # #         g = geocoder.ip('me')
# # #         return g.latlng
# # #     except Exception as e:
# # #         print(f"Error getting location: {e}")
# # #         return None, None

# # # if __name__ == "__main__":
# # #     lat, lon = get_location()
# # #     if lat is not None and lon is not None:
# # #         get_current_weather(openweathermap_api_key, lat, lon)


# # import requests
# # import geocoder

# # # Replace 'YOUR_OPENWEATHERMAP_API_KEY' with your OpenWeatherMap API key
# # openweathermap_api_key = '4a3bbb5e3ddb2d1f05d0d93c07cc97ed'

# # def get_current_weather(api_key, lat, lon):
# #     weather_api_url = 'http://api.openweathermap.org/data/2.5/weather'
# #     params = {
# #         'lat': lat,
# #         'lon': lon,
# #         'appid': api_key,
# #         'units': 'metric'  # You can change this to 'imperial' for Fahrenheit
# #     }

# #     try:
# #         response = requests.get(weather_api_url, params=params)
# #         data = response.json()
# #         print(data)

# #         if 'weather' in data:
# #             weather_description = data['weather'][0]['description']
# #             temperature = data['main']['temp']
# #             location = data['name']
# #             print(f"Weather in {location}: {weather_description}")
# #             print(f"Temperature: {temperature}°C")
# #         else:
# #             print("No weather data found in the response.")
# #     except Exception as e:
# #         print(f"Error getting weather data: {e}")

# # def get_location():
# #     try:
# #         g = geocoder.ip('me')
# #         return g.latlng
# #     except Exception as e:
# #         print(f"Error getting location: {e}")
# #         return None, None

# # if __name__ == "__main__":
# #     lat, lon = get_location()
# #     if lat is not None and lon is not None:
# #         get_current_weather(openweathermap_api_key, lat, lon)




import requests
import geocoder

# Replace 'YOUR_WEATHERSTACK_API_KEY' with your Weatherstack API key
weatherstack_api_key = 'c845e2123ed0577865dcdd8919db632c'

def get_current_weather(api_key):
    try:
        g = geocoder.ip('me')
        latitude, longitude = g.latlng

        if latitude and longitude:
            base_url = 'http://api.weatherstack.com/current'
            params = {
                'access_key': api_key,
                'query': f"{latitude},{longitude}"
            }

            response = requests.get(base_url, params=params)
            data = response.json()
            location = data['location']['name']
            temperature = data['current']['temperature']
            weather_description = data['current']['weather_descriptions'][0]
            print(f"Weather in {location}: {weather_description}")
            print(f"Temperature: {temperature}°C")
        else:
            print("Could not determine your location.")
    except Exception as e:
        print(f"Error getting weather data: {e}")

if __name__ == "__main__":
    get_current_weather(weatherstack_api_key)
















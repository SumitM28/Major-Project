import requests
import geocoder
location = geocoder.ip('me')

# Replace 'YOUR_WEATHERSTACK_API_KEY' with your Weatherstack API key
weatherstack_api_key = 'c845e2123ed0577865dcdd8919db632c'

def get_current_weather(api_key, latitude, longitude):
    base_url = 'http://api.weatherstack.com/current'
    params = {
        'access_key': api_key,
        'query': f"{latitude},{longitude}"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        location = data['location']['name']
        temperature = data['current']['temperature']
        weather_description = data['current']['weather_descriptions'][0]
        print(f"Weather in {location}: {weather_description}")
        print(f"Temperature: {temperature}°C")
    except Exception as e:
        print(f"Error getting weather data: {e}")

if __name__ == "__main__":
    # Replace with your actual latitude and longitude
    latitude, longitude = location.latlng
    # latitude = 27.1740
    # longitude = 77.9139
    get_current_weather(weatherstack_api_key, latitude, longitude)


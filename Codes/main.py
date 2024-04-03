import requests
import geocoder
from gtts import gTTS
import os
import pygame
import time


# Replace 'YOUR_WEATHERSTACK_API_KEY' with your Weatherstack API key
weatherstack_api_key = 'c845e2123ed0577865dcdd8919db632c'

# generate audio function

def generate_audio(location, weather_description,temperature):
    text = f"The weather in {location} is {weather_description} with a temperature of {temperature}°C. Enjoy your day!"
    tts = gTTS(text)
    mp3_file = "output.mp3"
    tts.save(mp3_file)
    
    # Initialize the pygame mixer
    pygame.mixer.init()
    # load the file 
    pygame.mixer.music.load(mp3_file)

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running while the audio plays
    while pygame.mixer.music.get_busy():
        pass
   

# weather function
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
        generate_audio(location,weather_description,temperature)
    except Exception as e:
        print(f"Error getting weather data: {e}")

# Function to make API requests
def make_api_request(latitude, longitude):
    # Replace 'YOUR_API_ENDPOINT' with the actual API endpoint you want to request
    api_endpoint = 'https://gps-backend-f881.onrender.com/'
    
    # Make the API request
    response = requests.put(api_endpoint, {
        "id":"656315e06f72dc93e399ead8",
        "latitude":latitude,
        "longitude":longitude
    })
    
    # Process the response data as needed
    data = response.json()
    print(data)

if __name__ == "__main__":
    location = geocoder.ip('me')
    latitude, longitude = location.latlng
    # latitude= 27.1725294
    # longitude = 77.9149155
    get_current_weather(weatherstack_api_key, latitude, longitude)
    while True:
        location = geocoder.ip('me')
        latitude, longitude = location.latlng
        make_api_request(latitude, longitude)
        time.sleep(10) 
    
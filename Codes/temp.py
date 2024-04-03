import requests
import time

# Function to make API requests
def make_api_request():
    # Replace 'YOUR_API_ENDPOINT' with the actual API endpoint you want to request
    api_endpoint = 'https://gps-backend-f881.onrender.com/656315e06f72dc93e399ead8'
    
    # Make the API request
    response = requests.get(api_endpoint)
    
    # Process the response data as needed
    data = response.json()
    print(data)

# Main loop with a 10-second time interval
while True:
    make_api_request()
    time.sleep(10)  # Pause for 10 seconds before the next request

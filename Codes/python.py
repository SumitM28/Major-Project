import geocoder

def get_current_location():
    try:
        # Get your current location based on your IP address
        location = geocoder.ip('me')

        if location:
            print(f"Your current location: {location.address}")
            print(f"Latitude: {location.latlng[0]}, Longitude: {location.latlng[1]}")
        else:
            print("Unable to determine your current location.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_current_location()
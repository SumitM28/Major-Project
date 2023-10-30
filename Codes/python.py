import geocoder

location = geocoder.ip('me')
latitude, longitude = location.latlng

print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")
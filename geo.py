import requests

try:
    # Use IP-API for fetching location details
    response = requests.get('http://ip-api.com/json/')
    data = response.json()

    if data['status'] == 'success':
        print("Your Location (Approximate):")
        print(f"Latitude: {data['lat']}")
        print(f"Longitude: {data['lon']}")
        print(f"City: {data['city']}")
        print(f"Region: {data['regionName']}")
        print(f"Country: {data['country']}")
    else:
        print("Failed to fetch location. Status:", data.get('message', 'Unknown error.'))
except Exception as e:
    print(f"An error occurred: {e}")

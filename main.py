import json

import requests

url = "https://os.smartcommunitylab.it/core.mobility/bikesharing/trento"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

string_response = response.text
print("Response:", string_response)

bike_station = json.loads(string_response)

print("Bike Stations:", len(bike_station))

# Total Slots
total_slots = 0

for station in bike_station:
    total_slots += station['totalSlots']

print("Total Slots:", total_slots)

# Other cool way too transform json, compact way
total_slots = sum(station['totalSlots'] for station in bike_station)
print("Total Slots (compact way):", total_slots)


# Free Slots
free_slots = sum(station['slots'] for station in bike_station)
print("Free Slots:", free_slots)

# Bikes
bikes = sum(station['bikes'] for station in bike_station)
print("Bikes:", bikes)
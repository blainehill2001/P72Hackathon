import requests
import json
import csv

with open('keys.json', 'r') as keys:
    keys = json.load(keys)
api_key = keys['GOOGLE_API_KEY']

def get_attraction_locations(attraction_names):
    """
    Converts a list of known location strings into lists of location strings and their coordinates
    """
    locations = []
    with open('data/attractions_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Tourist_Attractions'] in attraction_names:
                name = row['Tourist_Attractions']
                lat = float(row['Latitude'])
                lon = float(row['Longitude'])
                locations.append((name, (lat, lon)))
    return locations

def get_minutes_from_duration_string(duration):
    """
    Converts a duration string from GoogleMapsAPI into a float for minutes
    """
    return round(int(duration[:len(duration) - 1])/60, 2)

def compute_route_matrix(api_key, origins, destinations):
    """
    Takes a list of origin and destination coordinates and 
    returns Routes API information for each pair between origin and destination
    """
    url = 'https://routes.googleapis.com/distanceMatrix/v2:computeRouteMatrix'
    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': api_key,
        'X-Goog-FieldMask': 'originIndex,destinationIndex,duration,distanceMeters,status,condition,travelAdvisory.transitFare'
    }
    data = {
        "origins": [{"waypoint": {"location": {"latLng": {"latitude": lat, "longitude": lon}}}} for lat, lon in origins],
        "destinations": [{"waypoint": {"location": {"latLng": {"latitude": lat, "longitude": lon}}}} for lat, lon in destinations],
        "travelMode": "TRANSIT"
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

def calculate_all_routes(api_key, landmarks):
    """
    Takes a list of landmark names and returns the time, in minutes, between each pair of landmarks
    """
    landmarks = get_attraction_locations(landmarks)
    landmark_coords = [coords for name, coords in landmarks]
    routes = compute_route_matrix(api_key, landmark_coords, landmark_coords)
    actual_routes = [route for route in routes if route["condition"] == "ROUTE_EXISTS"]
    return [(landmarks[int(route["originIndex"])][0], landmarks[int(route["destinationIndex"])][0], get_minutes_from_duration_string(route["duration"])) for route in actual_routes]

landmarks = ["The Vessel", "Empire State Building", "Times Square", "Rockefeller Center"]
print(calculate_all_routes(api_key, landmarks))

# Returns in the form of a list [("origin", "destination", trip duration (minutes))]
# [('Rockefeller Center', 'Times Square', 11.13), ('Times Square', 'Rockefeller Center', 10.02), ('Times Square', 'The Vessel', 14.2), ('The Vessel', 'Times Square', 13.45), ('Empire State Building', 'Times Square', 12.2), ('The Vessel', 'Empire State Building', 17.08), ('The Vessel', 'Rockefeller Center', 21.75), ('Empire State Building', 'The Vessel', 17.93), ('Empire State Building', 'Rockefeller Center', 11.85), ('Rockefeller Center', 'Empire State Building', 15.83), ('Times Square', 'Empire State Building', 11.7), ('Rockefeller Center', 'The Vessel', 19.3)]
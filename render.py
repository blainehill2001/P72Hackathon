import tkinter as tk
from tkinter import scrolledtext
import requests
import json
import csv
import networkx as nx
import time
import random

api_key = "AIzaSyBF1v47rTxjmm0LEBx-vtO5IDWYvlUBBcA"
landmarks = ['Rockefeller Center', 'The Vessel', 'Empire State Building', 'Times Square']
class Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_edge(self, start, end, distance):
        self.graph.add_edge(start, end, weight=distance)

    def minimum_spanning_tree(self):
        mst = nx.minimum_spanning_tree(self.graph)
        return mst

    def dfs(self, start):
        visited = set()
        order = []
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                stack.extend(neighbor for neighbor in self.graph[node] if neighbor not in visited)
        return order

def get_attraction_locations(attraction_names):
    locations = []
    with open('attractions_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Tourist_Attractions'] in attraction_names:
                name = row['Tourist_Attractions']
                lat = float(row['Latitude'])
                lon = float(row['Longitude'])
                locations.append((name, (lat, lon)))
    return locations

def get_minutes_from_duration_string(duration):
    return round(int(duration[:len(duration) - 1])/60, 2)

def compute_route_matrix(api_key, origins, destinations):
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
    landmarks = get_attraction_locations(landmarks)
    landmark_coords = [coords for name, coords in landmarks]
    routes = compute_route_matrix(api_key, landmark_coords, landmark_coords)
    actual_routes = [route for route in routes if route["condition"] == "ROUTE_EXISTS"]
    return [(landmarks[int(route["originIndex"])][0], landmarks[int(route["destinationIndex"])][0], get_minutes_from_duration_string(route["duration"])) for route in actual_routes]

class LandmarksApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorted Landmarks")
        self.landmarks = ['Rockefeller Center', 'The Vessel', 'Empire State Building', 'Times Square']  # Define landmarks here
        
        self.scroll_text = scrolledtext.ScrolledText(self.root, width=40, height=10)
        self.scroll_text.pack(expand=True, fill='both')
        
        self.update_button = tk.Button(self.root, text="Update", command=self.update_sorted_order)
        self.update_button.pack()
        
        # Schedule automatic update every 5 seconds (5000 milliseconds)
        self.root.after(500, self.auto_update_sorted_order)
        
    def update_sorted_order(self):
        sorted_order = self.get_sorted_order()
        self.scroll_text.delete('1.0', tk.END)
        for i, landmark in enumerate(sorted_order, 1):
            self.scroll_text.insert(tk.END, f"{i}. {landmark}\n")
    
    def auto_update_sorted_order(self):
        self.update_sorted_order()
        # Schedule the next automatic update
        self.root.after(500, self.auto_update_sorted_order)
    
    def get_sorted_order(self):
        graph = Graph()
        data = calculate_all_routes(api_key, self.landmarks)
        
        for start, end, distance in data:
            graph.add_edge(start, end, distance)
        
        mst = graph.minimum_spanning_tree()
        start_landmark = self.landmarks[0]
        sorted_order = graph.dfs(start_landmark)
        
        return sorted_order

root = tk.Tk()
app = LandmarksApp(root)
root.mainloop()

import graph_cleaned
import pandas as pd

attractions_df = pd.read_csv('attractions_data.csv')
subways_df = pd.read_csv('subways_data.csv')
walking_route_df = pd.read_csv('walking_route_data.csv')
subway_route_df = pd.read_csv('subway_route_data.csv')

graph = graph_cleaned.Graph()
for place in attractions_df['Tourist_Attractions']:
  la = attractions_df[attractions_df.Tourist_Attractions == place]['Latitude']
  lo = attractions_df[attractions_df.Tourist_Attractions == place]['Longitude']
  graph.add_node(lo.item(), la.item())

for station in subways_df['Station_Names']:
  la = subways_df[subways_df.Station_Names == station]['Latitude']
  lo = subways_df[subways_df.Station_Names == station]['Longitude']
  graph.add_node(lo.item(), la.item())

for place in walking_route_df['Tourist_Attractions']:
  la_place = attractions_df[attractions_df.Tourist_Attractions == place]['Latitude'].item()
  lo_place = attractions_df[attractions_df.Tourist_Attractions == place]['Longitude'].item()
  
  for i in range(len(walking_route_df[walking_route_df.Tourist_Attractions == place]['Subway_Stations'].item().strip("[]").split(','))):
    station = walking_route_df[walking_route_df.Tourist_Attractions == place]['Subway_Stations'].item().strip("[]").split(',')[i]
    if i == 0: station = station[1:-1]
    else: station = station[2:-1]
    la_station = subways_df[subways_df.Station_Names == station]['Latitude'].item()
    lo_station = subways_df[subways_df.Station_Names == station]['Longitude'].item()

    graph.add_edge(graph.find_node(lo_place, la_place), graph.find_node(lo_station, la_station))

for station1 in subway_route_df['From']:
  la_station1 = subways_df[subways_df.Station_Names == station1]['Latitude'].item()
  lo_station1 = subways_df[subways_df.Station_Names == station1]['Longitude'].item()

  for i in range(len(subway_route_df[subway_route_df.From == station1]['To'].item().strip("[]").split(","))):
    station2 = subway_route_df[subway_route_df.From == station1]['To'].item().strip("[]").split(",")[i]
    if i == 0: station2 = station2[1:-1]
    else: station2 = station2[2:-1]
    la_station2 = subways_df[subways_df.Station_Names == station2]['Latitude'].item()
    lo_station2 = subways_df[subways_df.Station_Names == station2]['Longitude'].item()

    graph.add_edge(graph.find_node(lo_station1, la_station1), graph.find_node(lo_station2, la_station2))

graph_cleaned.plot_graph(graph)
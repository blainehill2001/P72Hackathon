import pandas as pd

attractions_data = {
    'Tourist_Attractions': ['The Vessel', 'Empire State Building', 'Times Square', 'Rockefeller Center', 'Grand Central Terminal', 'Chelsea Market', 'Madison Square Garden', 'United Nations Headquarters'],
    'Latitude':  [ 40.753813,  40.748441,  40.757982,  40.758737,  40.753324,  40.742427,  40.750503,  40.749330],
    'Longitude': [-74.002155, -73.985665, -73.985538, -73.978675, -73.976801, -74.006142, -73.993438, -73.967921]
}

attractions_df = pd.DataFrame(attractions_data)

attractions_df.to_csv('attractions_data.csv', index=False)

print("DataFrame saved to CSV file.")
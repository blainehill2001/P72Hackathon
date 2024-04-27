import pandas as pd

walking_route = {
    'Tourist_Attractions': ['The Vessel',
                            'Empire State Building', 
                            'Times Square', 
                            'Rockefeller Center', 
                            'Grand Central Terminal',
                            'Chelsea Market',
                            'Madison Square Garden',
                            'United Nations Headquarters'],
    
    'Subway_Stations': [['34 St - Hudson Yards', '34 St - Penn Station 1'],
                        ['34 St - Herald Sq', '33 St'],
                        ['Times Sq - 42 St', '42 St - Port Authority Bus Terminal'],
                        ['47-50 Sts - Rockefeller Ctr', '5 Av', '5 Av/53 St'],
                        ['Grand Central - 42 St'],
                        ['14 St/8 Av'],
                        ['34 St - Penn Station 1', '34 St - Penn Station 2'],
                        ['Grand Central - 42 St']]               
}

walking_route_df = pd.DataFrame(walking_route)

walking_route_df.to_csv('walking_route_data.csv', index=False)

print("DataFrame saved to CSV file.")
import pandas as pd

subway_route = {
    'From': ['50 St 1', '7 Av', '50 St 2',
             '49 St', '47-50 Sts - Rockefeller Ctr', '5 Av/53 St',
             '51 St', '42 St - Port Authority Bus Terminal', 
             'Times Sq - 42 St', 
             '42 St - Bryant Pk', '5 Av','Grand Central - 42 St', '34 St - Hudson Yards',
             '34 St - Penn Station 1', '34 St - Penn Station 2', '34 St - Herald Sq', '28 St 2', '33 St', '23 St 1', '23 St 2', '18 St', '23 St 3',
             '23 St 4', '28 St 3', '23 St 5', '14 St/8 Av', '14 St/6 Av', '14 St - Union Sq', 
             '28 St 1'],
    
    'To': [['42 St - Port Authority Bus Terminal', '7 Av'], ['47-50 Sts - Rockefeller Ctr'], ['Times Sq - 42 St'],
           ['Times Sq - 42 St'], ['5 Av/53 St', '42 St - Bryant Pk'], ['Lexington Av/53 St'],
           ['Grand Central - 42 St'], ['34 St - Penn Station 1'], 
           ['34 St - Penn Station 2', '5 Av', '34 St - Herald Sq', 'Grand Central - 42 St'], 
           ['34 St - Herald Sq'], ['Grand Central - 42 St'], ['33 St'], ['Times Sq - 42 St'],
           ['23 St 1'], ['28 St 1'], ['28 St 2', '23 St 3'], ['23 St 4'], ['28 St 3'], ['14 St/8 Av'], ['18 St'], ['14 St'], ['14 St/6 Av'],
           ['14 St - Union Sq'], ['23 St 5'], ['14 St - Union Sq'], ['14 St/6 Av', 'W 4 St - Wash Sq'], ['W 4 St - Wash Sq', '14 St - Union Sq'], ['8 St - NYU', 'Astor Pl'],
           ['23 St 2']]
}

subway_route_df = pd.DataFrame(subway_route)

subway_route_df.to_csv('subway_route_data.csv', index=False)

print("DataFrame saved to CSV file.")
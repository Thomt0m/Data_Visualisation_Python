import json

from plotly.graph_objects import Scattergeo, Layout
from plotly import offline



filename = 'Data/Earthquakes/eq_data_30_day_m1.json'


with open(filename) as file:
    eq_data = json.load(file)

# Get the title of the file
fig_title = 'Global Earthquakes'
try:
    fig_title = eq_data['metadata']['title']
except:
    print('Failed to read title from metadata')



# Get the data (dictionary) for each individual earthquake (feature) from the file data
eq_dicts = eq_data['features']

# Data to retrieve
eq_magnitudes = []
eq_longitude = []
eq_latitude = []
eq_title = []

# Retrieve the desired data from each dictionary
for eq_dict in eq_dicts:
    eq_magnitudes.append(   eq_dict['properties']['mag']            )
    eq_title.append(        eq_dict['properties']['title']          )
    eq_longitude.append(    eq_dict['geometry']['coordinates'][0]   )
    eq_latitude.append(     eq_dict['geometry']['coordinates'][1]   )




# Create a world-map showing the earthquake data
data = [{

    'type'  :   'scattergeo',
    'lon'   :   eq_longitude,
    'lat'   :   eq_latitude,
    'text'  :   eq_title,

    'marker':{
        'size' : [3*mag for mag in eq_magnitudes],
        'color': eq_magnitudes,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]

my_layout = Layout(title=fig_title)

fig = { 'data':data, 'layout':my_layout}

offline.plot(fig, filename='Global_Earthquakes.html')
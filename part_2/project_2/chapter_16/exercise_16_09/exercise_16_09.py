# Exercise 16-9

import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Extract data from csv file and store into a list
filename = 'world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    next(reader)

    # Use indexes retrieved by printing first line
    lats, lons, bris = [], [], []
    for row in reader:
        lats.append(float(row[0]))
        lons.append(float(row[1]))
        bris.append(float(row[2]))

# Map world fires
data = [{
    'type': 'scattergeo',
    'lat': lats,
    'lon': lons,
    'marker': {
        'size': 8,
        'color': bris,
        'colorscale': 'Oranges',
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title='World Fires')
offline.plot({'data': data, 'layout': my_layout}, filename='exercise_16_09.html')
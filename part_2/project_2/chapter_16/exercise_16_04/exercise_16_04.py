# Exercise 16-4

import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    name_index = header_row.index('NAME')
    date_index = header_row.index('DATE')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')

    # Get all info from csv file
    dates, highs, lows = [], [], []
    for row in reader:
        name = row[name_index]
        date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            pass
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

# Visualize plot
plt.style.use('bmh')
fig, ax = plt.subplots(figsize=(16, 9))
ax.plot(dates, highs, c='red', linewidth=1)
ax.plot(dates, lows, c='blue', linewidth=1)
plt.fill_between(dates, highs, lows, facecolor='orange', alpha=0.1)

# Set text and labels for plot
plt.title(f"Daily high and low temperatures, {name} - 2018", fontsize=28)
plt.xlabel('', fontsize=20)
fig.autofmt_xdate()
plt.ylabel("Temperature", fontsize=20)
plt.tick_params(axis='both', labelsize=11)

plt.show()
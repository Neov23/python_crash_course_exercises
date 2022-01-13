# Exercise 16-2

import csv
from datetime import datetime

import matplotlib.pyplot as plt

# Extract all info about Sitka's weather from csv file
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    next(reader)

    # Store date and high temperatures in Sitka for 2018 in lists
    s_dates, s_highs, s_lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[2])
        low = int(row[6])
        s_dates.append(date)
        s_highs.append(high)
        s_lows.append(low)

# Extract all info about Death Valley's weather from csv file
filename = 'death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    next(reader)

    # Store high temperatures in Death Valley for 2018 in lists
    dv_dates, dv_highs, dv_lows = [], [], []
    for row in reader:
        try:
            date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[4])
            low = int(row[5])
            dv_dates.append(date)
            dv_highs.append(high)
            dv_lows.append(low)
        except ValueError:
            pass

# Visualize plot
plt.style.use('bmh')
fig, ax = plt.subplots(figsize=(16, 9))
ax.plot(s_dates, s_highs, c='red', alpha=0.5)
ax.plot(s_dates, s_lows, c='blue', alpha=0.5)
ax.plot(dv_dates, dv_highs, c='red', alpha=0.5)
ax.plot(dv_dates, dv_lows, c='blue', alpha=0.5)
plt.fill_between(s_dates, s_highs, s_lows, facecolor='green', alpha=0.1)
plt.fill_between(dv_dates, dv_highs, dv_lows, facecolor='orange', alpha=0.1)

plt.title("Daily high and low temperatures (Sitka and Death Valley) - 2018",
    fontsize=26)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature", fontsize=16)
plt.tick_params(labelsize=12)

plt.show()
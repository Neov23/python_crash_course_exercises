# Exercise 16-1

import csv
from datetime import datetime

import matplotlib.pyplot as plt

# Extract all info from csv file about Sitka weather
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    next(reader)

    # Create lists with dates and rainfalls for Sitka in 2018
    dates, rainfalls = [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        rainfall = float(row[3])
        dates.append(date)
        rainfalls.append(rainfall)

# Visualize plot
plt.style.use('bmh')
fig, ax = plt.subplots(figsize=(16, 9))
ax.plot(dates, rainfalls, c='blue')

plt.title("Daily Rainfalls in Sitka for the Year 2018", fontsize=26)
plt.xlabel("Date", fontsize=20)
fig.autofmt_xdate()
plt.ylabel("Rainfall", fontsize=20)
plt.tick_params(axis='both', labelsize=12)

plt.show()
# Downloading Data

- [Exercise 16-1](exercise_16_01/exercise_16_01.py):
Sitka is in a temperate rainforest, so it gets a fair amount of rainfall. In
the data file sitka_weather_2018_simple.csv is a header called PRCP, which
represents daily rainfall amounts. Make a visualization focusing on the data
in this column. You can repeat the exercise for Death Valley if you’re curious
how little rainfall occurs in a desert.

- [Exercise 16-2](exercise_16_02/exercise_16_02.py):
The temperature scales on the Sitka and Death Valley graphs reflect the
different data ranges. To accurately compare the temperature range in Sitka to
that of Death Valley, you need identical scales on the y-axis. Change the
settings for the y-axis on one or both of the charts in Figures 16-5 and 16-6.
Then make a direct comparison between temperature ranges in Sitka and Death
Valley (or any two places you want to compare).
The pyplot function ylim() allows you to set the limits of just the y-axis.
If you ever need to specify the limits of the x-axis, there’s a corresponding
xlim() function as well.

- [Exercise 16-4](exercise_16_04/exercise_16_04.py):
In this section, we hardcoded the indexes corresponding to the TMIN and TMAX
columns. Use the header row to determine the indexes for these values, so your
program can work for Sitka or Death Valley. Use the station name to
automatically generate an appropriate title for your graph as well.

- [Exercise 16-6](exercise_16_06/exercise_16_06.py):
The loop that pulls data from all_eq_dicts uses variables for the magnitude,
longitude, latitude, and title of each earthquake before appending these
values to their appropriate lists. This approach was chosen for clarity in how
to pull data from a JSON file, but it’s not necessary in your code. Instead of
using these temporary variables, pull each value from eq_dict and append it to
the appropriate list in one line. Doing so should shorten the body of this
loop to just four lines.

- [Exercise 16-7](exercise_16_07/exercise_16_07.py):
In this section, we specified the title manually when defining my_layout,
which means we have to remember to update the title every time the source file
changes. Instead, you can use the title for the data set in the metadata part
of the JSON file. Pull this value, assign it to a variable, and use this for
the title of the map when you’re defining my_layout.

- [Exercise 16-9](exercise_16_09/exercise_16_09.py):
In the resources for this chapter, you’ll find a file called
world_fires_1_day.csv. This file contains information about fires burning in
different locations around the globe, including the latitude and longitude,
and the brightness of each fire. Using the data processing work from the first
part of this chapter and the mapping work from this section, make a map that
shows which parts of the world are affected by fires.

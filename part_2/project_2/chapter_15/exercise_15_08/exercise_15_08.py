# Exercise 15-8

from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice import Dice

# Create two D6 dices
dice_1 = Dice()
dice_2 = Dice()

# Roll the dices 50.000 times, multiply and store each result in a list
results = []
for roll_num in range(50_000):
    result = dice_1.roll_dice() * dice_2.roll_dice()
    results.append(result)

# Count the times each value appears in results and store info in a list
max_result = dice_1.num_sides * dice_2.num_sides

frequencies = []
for value in range(1, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
possibilities = list(range(1, max_result + 1))
data = [Bar(x=possibilities, y= frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling multiplying two D6 50.000 times',
    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='exercise_15_08')
# Exercise 15-9

from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice import Dice

# Create two D6 dices
dice_1 = Dice()
dice_2 = Dice()

# Roll the dices 50.000 times and store each result in a list
results = [dice_1.roll_dice() + dice_2.roll_dice() for x in range(50_000)]

# Count the times each value appears in results and store info in a list
max_result = dice_1.num_sides + dice_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]

# Visualize the results
possibilities = list(range(2, max_result + 1))
data = [Bar(x=possibilities, y= frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 dices 50.000 times',
    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='exercise_15_09.html')
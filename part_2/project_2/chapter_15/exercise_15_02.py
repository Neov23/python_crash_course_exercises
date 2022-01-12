# Exercise 15-2

import matplotlib.pyplot as plt

numbers = range(1, 5001)
cubes = [number**3 for number in numbers]

# Set plot
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.scatter(numbers, cubes, c=cubes, cmap=plt.cm.Greens, s=8)

# Set title and label for the axes
ax.set_title("Cubes", fontsize=26)
ax.set_xlabel("Value", fontsize=16)
ax.set_ylabel("Cube of Value", fontsize=16)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=9)

plt.show()
# Exercise 15-1

import matplotlib.pyplot as plt

numbers = range(1, 1001)
cubes = [number**3 for number in numbers]

# Create plot
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.plot(numbers, cubes, linewidth=2)

# Set title and labels for the axes
ax.set_title("Cubes")
ax.set_xlabel("Value")
ax.set_ylabel("Cube of Value")

plt.show()
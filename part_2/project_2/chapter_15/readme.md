# Generating Data

- [Exercise 15-1](exercise_15_01.py):
A number raised to the third power is a cube. Plot the first five cubic
numbers, and then plot the first 5000 cubic numbers.

- [Exercise 15-2](exercise_15_02.py):
Apply a colormap to your cubes plot.

- [Exercise 15-3](exercise_15_03/exercise_15_03.py):
Modify rw_visual.py by replacing ax.scatter() with ax.plot(). to simulate the
path of a pollen grain on the surface of a drop of water, pass in the
rw.x_values and rw.y_values, and include a linewidth argument. Use 5000 instead
of 50,000 points.
**Modules:**
  - [random_walk.py](exercise_15_03/random_walk.py)

- [Exercise 15-4](exercise_15_04/exercise_15_04.py):
In class `RandomWalk`, the x_step and y_step are generated from the same
condition summary. The direction is chosen randomly from [1, -1] and the
distance from the list [0, 1, 2, 3, 4]. Modify the values in these lists to
see what happens to your walking plots. Try a list with more choices for
distance, for example 0 to 8, or aferese the number "1" from the direction
list of x or y.
**Modules:**
  - [random_walk.py](exercise_15_04/random_walk.py)

- [Exercise 15-5](exercise_15_05/exercise_15_05.py):
The method fill_walk() is lengthy. Create a new method called get_step() to
determine the direction and distance for each step, and then calculate the
step. You should end up with two calls to get_step() in fill_walk():
`x_step = self.get_step()`
`y_step = self.get_step()`
This refactoring should reduce the size of fill_walk() and make the method
easier to read and understand.
**Modules:**
  - [random_walk.py](exercise_15_05/random_walk.py)

- [Exercise 15-6](exercise_15_06/exercise_15_06.py):
Create a simulation showing what happens when you roll two eight-sided dice
1000 times. Try to picture what you think the visualization will look
like before you run the simulation; then see if your intuition was correct.
Gradually increase the number of rolls until you start to see the limits of
your system’s capabilities.
**Modules:**
  - [dice.py](exercise_15_06/dice.py)

- [Exercise 15-7](exercise_15_07/exercise_15_07.py):
If you roll three D6 dice, the smallest number you can roll is 3 and the
largest number is 18. Create a visualization that shows what happens when you
roll three D6 dice.
**Modules:**
  - [dice.py](exercise_15_07/dice.py)

- [Exercise 15-8](exercise_15_08/exercise_15_08.py):
When you roll two dice, you usually add the two numbers together to get the
result. Create a visualization that shows what happens if you multiply these
numbers instead.
**Modules:**
  - [dice.py](exercise_15_08/dice.py)

- [Exercise 15-9](exercise_15_09/exercise_15_09.py):
For clarity, the listings in this section use the long form of for loops. If
you’re comfortable using list comprehensions, try writing a comprehension for
one or both of the loops in each of these programs.
**Modules:**
  - [dice.py](exercise_15_09/dice.py)

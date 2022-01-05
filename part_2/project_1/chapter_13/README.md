# Aliens

- [Exercise 13-1](exercise_13_01/exercise_13_01.py):
Find an image of a star . Make a grid of stars appear on the screen.
**Modules:**
  - [star.bmp](exercise_13_01/star.bmp)
  - [star.py](exercise_13_01/star.py)

- [Exercise 13-2](exercise_13_02/exercise_13_02.py):
You can make a more realistic star pattern by introducing randomness when you
place each star. Recall thatyou can get a random number like this:
from random import randint
random_number = randint(-10, 10)
This code returns a random integer between -10 and 10. Using your code in
Exercise 13-1, adjust each star’s position by a random amount.
**Modules:**
  - [star.bmp](exercise_13_02/star.bmp)
  - [star.py](exercise_13_02/star.py)

- [Exercise 13-4](exercise_13_04/exercise_13_04.py):
Modify your code in Exercise 13-3 so when a row of raindrops disappears off
the bottom of the screen, a new row appears at the top of the screen and
begins to fall.
**Modules:**
  - [raindrop.bmp](exercise_13_04/raindrop.bmp)
  - [raindrop.py](exercise_13_04/raindrop.py)

- [Exercise 13-5](exercise_13_05/exercise_13_05.py):
We’ve come a long way since Exercise 12-6, Sideways Shooter. For this
exercise, try to develop Sideways Shooter to the same point we’ve brought
Alien Invasion to. Add a fleet of aliens, and make them move sideways toward
the ship. Or, write code that places aliens at random positions along the
right side of the screen and then sends them toward the ship. Also, write code
that makes the aliens disappear when they’re hit.
**Modules:**
  - [rocket.bmp](exercise_13_05/rocket.bmp)
  - [alien.bmp](exercise_13_05/alien.bmp)
  - [rocket.py](exercise_13_05/rocket.py)
  - [bullet.py](exercise_13_05/bullet.py)
  - [alien.py](exercise_13_05/alien.py)

- [Exercise 13-6](exercise_13_06/exercise_13_06.py):
In Sideways Shooter, keep track of the number of times the ship is hit and the
number of times an alien gets past the ship. Decide on an appropriate condition
for ending the game, and stop the game when this situation occurs.
**Modules:**
  - [rocket.bmp](exercise_13_05/rocket.bmp)
  - [alien.bmp](exercise_13_05/alien.bmp)
  - [rocket.py](exercise_13_05/rocket.py)
  - [bullet.py](exercise_13_05/bullet.py)
  - [alien.py](exercise_13_05/alien.py)

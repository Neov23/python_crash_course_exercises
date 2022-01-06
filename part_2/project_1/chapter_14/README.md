# Scoring

- [Exercise 14-1](exercise_14_01/README.md):
Because Alien Invasion uses keyboard input to control the ship, it would be
useful to start the game with a keypress. Add code that lets the player press
P to start. It might help to move some code from "_check_play_button()" to a
"_start_game()" method that can be called from "_check_play_button()" and
"_check_keydown_events()".
**Modules:**
  - [alien.py](exercise_14_01/alien.py)
  - [bullet.py](exercise_14_01/bullet.py)
  - [button.py](exercise_14_01/button.py)
  - [game_stats.py](exercise_14_01/game_stats.py)
  - [settings.py](exercise_14_01/settings.py)
  - [ship.py](exercise_14_01/ship.py)

- [Exercise 14-2](exercise_14_02/exercise_14_02.py):
Create a rectangle at the right edge of the screen that moves up and down at a
steady rate. Then have a ship appear on the left side of the screen that the
player can move up and down while firing bullets at the moving, rectangular
target. Add a Play button that starts the game, and when the player misses the
target three times, end the game and make the Play button reappear. Let the
player restart the game with this Play button.
**Modules:**
  - [bullet.py](exercise_14_02/bullet.py)
  - [button.py](exercise_14_02/button.py)
  - [enemy.py](exercise_14_02/enemy.py)
  - [rocket.py](exercise_14_02/rocket.py)
  - [rocket.bmp](exercise_14_02/rocket.bmp)

- [Exercise 14-3](exercise_14_03/exercise_14_03.py):
Start with your work from Exercise 14-2 (page 285). Make the target move
faster as the game progresses, and restart the target at the original speed
when the player clicks Play.
**Modules:**
  - [bullet.py](exercise_14_03/bullet.py)
  - [button.py](exercise_14_03/button.py)
  - [enemy.py](exercise_14_03/enemy.py)
  - [rocket.py](exercise_14_03/rocket.py)
  - [rocket.bmp](exercise_14_03/rocket.bmp)

- [Exercise 14-4](exercise_14_04exercise_14_04.py):
Make a set of buttons for Alien Invasion that allows the player to select an
appropriate starting difficulty level for the game. Each button should assign
the appropriate values for attributes in Settings needed to create different
difficulty levels.
**Modules:**
  - [alien.py](exercise_14_04/alien.py)
  - [bullet.py](exercise_14_04/bullet.py)
  - [button.py](exercise_14_04/button.py)
  - [game_stats.py](exercise_14_04/game_stats.py)
  - [settings.py](exercise_14_04/settings.py)
  - [ship.py](exercise_14_04/ship.py)

- [Exercise 14-5](exercise_14_05.py):
The high score is reset every time a player closes and restarts Alien Invasion.
Fix this by writing the high score to a file before calling sys.exit() and
reading in the high score when initializing its value in GameStats.

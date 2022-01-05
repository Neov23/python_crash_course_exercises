# Exercise 12-4

import sys

import pygame

from rocket import Rocket

class RocketGame:
    """Overall class to manage the game"""

    def __init__(self):
        """Game initials"""
        pygame.init()

        # Screen settings
        self.screen = pygame.display.set_mode((1024, 768))
        pygame.display.set_caption("exercise_12_04")
        self.bg_color = (255, 255, 255)
        
        self.rocket = Rocket(self)

    def run_game(self):
        """Start the main loop of the game."""
        while True:
            self.events()
            self.rocket.update()
            self.update_screen()

    def events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._keyup_events(event)
    
    def _keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        
    def _keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def update_screen(self):
        """Update screen each time the loop replays"""
        self.screen.fill(self.bg_color)
        self.rocket.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance and run the game.
    main_game = RocketGame()
    main_game.run_game()
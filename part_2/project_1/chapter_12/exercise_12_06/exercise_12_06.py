# Exercise 12-6

import sys

import pygame

from rocket import Rocket
from bullet import Bullet

class RocketGame:
    """Overall class to manage the game"""

    def __init__(self):
        """Game initials"""
        pygame.init()

        self.screen = pygame.display.set_mode((1024, 768))
        pygame.display.set_caption("exercise_12_06")
        self.bg_color = (0, 0, 0)
        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop of the game."""
        while True:
            self.events()
            self.rocket.update()
            self._update_bullets() 
            self.update_screen()
            print(len(self.bullets))

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
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_SPACE:
            self.fire_bullets()
        elif event.key == pygame.K_q:
            sys.exit()
        
    def _keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
    
    def fire_bullets(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Update bullet position."""
        self.bullets.update()

        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.rocket.screen_rect.right:
                self.bullets.remove(bullet)

    def update_screen(self):
        """Update screen each time the loop replays"""
        self.screen.fill(self.bg_color)
        self.rocket.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance and run the game.
    rg = RocketGame()
    rg.run_game()
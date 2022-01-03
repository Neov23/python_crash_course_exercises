"""
I purposefully don't create an extra module, or class with settings, to
raise the difficulty, caused by complexity. I assume that makes my practice
more effective, even though i would always try (apart from these exercises)
to find the easiest way to create a project.
"""

# TASK_1: Check if bullets are deleting off screen
# TASK_2: Check if UFO's are deleting off screenq

import sys

import pygame
from pygame.sprite import Sprite

from rocket_2 import Rocket
from bullet_2 import Bullet
from alien_2 import Alien

from random import randint


class RocketGame:
    """Overall class to manage the game"""

    def __init__(self):
        """Game initials"""
        pygame.init()

        # Screen settings
        self.screen_width = 1280
        self.screen_height = 960
        self.bg_color = (0, 0, 0)

        self.screen = pygame.display.set_mode((self.screen_width,
        self.screen_height))
        pygame.display.set_caption("Sideways Rocket Game for exercise 13-5")
        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop of the game."""
        while True:
            self.events()
            self.rocket.update()
            self.update_bullets()
            self._update_aliens()
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
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullets()
        
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
    
    def update_bullets(self):
        # Update bullet position
        self.bullets.update()

        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.rocket.screen_rect.right:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

    def _update_aliens(self):
        """Update alien position"""
        self.aliens.update()
        
    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        rocket_width, rocket_height = self.rocket.rect.size
        available_space_x = self.screen_width - 4 * rocket_width
        number_columns = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen
        available_space_y = self.screen_height - 2 * alien_height
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for column_number in range(number_columns):
                self._create_alien(column_number, row_number)
    
    def _create_alien(self, number_alien_column, number_alien_row):
        """Create an alien and place it in the row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.rect.x = (self.screen_width - alien_width - 2 *
            alien_width * number_alien_column)
        alien.rect.y = (alien_height + 2 * alien_height * 
            number_alien_row)
        alien.x = alien.rect.x
        
        # Random choice to choose if alien will be created or not.
        # 75% possibility of spawn rate
        self.choice = randint(0, 3)
        if self.choice != 0:
            self.aliens.add(alien)
        

    def update_screen(self):
        """Update screen each time the loop replays"""
        self.screen.fill(self.bg_color)
        self.rocket.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game.
    rg = RocketGame()
    rg.run_game()
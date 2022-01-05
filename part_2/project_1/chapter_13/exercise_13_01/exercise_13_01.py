# Exercise 13-1

import sys

import pygame

from star import Star

class Space:
    """A program that displays the space with stars (objects)"""
    
    def __init__(self):
        """Initialize space"""
        pygame.init()
        
        # Screen settings
        self.screen_width = 1280
        self.screen_height = 960
        self.bg_color = (0, 0, 0)
        
        # Initialize window and screen display
        self.screen = pygame.display.set_mode((self.screen_width, 
        self.screen_height))
        pygame.display.set_caption("exercise_13_01")

        # Create a group of stars (objects)
        self.stars = pygame.sprite.Group()
        self.create_fleet()

    def run_game(self):
        """Start the main loop for the program"""
        while True:
            self.check_events()
            self._update_screen()
    
    def check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
    
    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_q:
            sys.exit()
    
    def create_fleet(self):
        """Create a fleet of stars"""
        # Space between each star is equal to half of a star's width
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.screen_width - star_width
        number_stars_x = int(available_space_x // (1.5 * star_width))

        # Define the number of rows of stars that fit on the screen
        available_space_y = self.screen_height - star_height
        number_stars_y = int(available_space_y // (1.5 * star_height))

        # Create the full fleet of stars
        for row_number in range(number_stars_y):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)
        
    def _create_star(self, star_number_x, star_number_y):
        """Create a star and place it in a certain position"""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.rect.x = star_width + star_number_x * star_width * 1.5
        star.rect.y = star_height + star_number_y * star_height * 1.5
        self.stars.add(star)
        
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    # Make a program instance, and run the game.
    main_program = Space()
    main_program.run_game()
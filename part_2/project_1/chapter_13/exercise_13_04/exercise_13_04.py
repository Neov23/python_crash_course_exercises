# Exercise 13-4

import sys

import pygame

from raindrop import Raindrop

class Sky:
    """A program that displays the sky with falling raindrops (objects)"""
    
    def __init__(self):
        """Initialize sky"""
        pygame.init()
        
        # Screen settings
        self.screen_width = 1280
        self.screen_height = 960
        self.bg_color = (20, 20, 50)
        
        # Initialize window and screen display
        self.screen = pygame.display.set_mode((self.screen_width, 
        self.screen_height))
        pygame.display.set_caption("exercise_13_04")

        # Create a group of raindrops (objects)
        self.raindrops = pygame.sprite.Group()
        self.create_fleet()

    def run_game(self):
        """Start the main loop for the program"""
        while True:
            self._check_events()
            self._update_raindrops()
            self._update_screen()
    
    def _check_events(self):
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
        """Create a fleet of raindrops"""
        # Space between each rainbow is equal to at least two raindrop's width
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        available_space_x = self.screen_width - raindrop_width
        number_raindrops_x = int(available_space_x // (2 * raindrop_width))

        # Define the number of rows of raindrops that fit on the screen
        available_space_y = self.screen_height
        number_rows = int(available_space_y // (2 * raindrop_height) + 1)

        # Create the full fleet of raindrops
        for row_number in range(number_rows):
            for raindrop_number in range(number_raindrops_x):
                self._create_raindrop(raindrop_number, row_number)
        
    def _create_raindrop(self, raindrop_number, row_number):
        """Create a raindrop and place it in a certain position"""
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        raindrop.rect.x = raindrop_width + raindrop_number * raindrop_width * 2
        raindrop.rect.y = raindrop_height + row_number * raindrop_height * 2
        self.raindrops.add(raindrop)
    
    def _recreate_raindrop(self):
        """When raindrop disappears below, it reappears above the screen"""
        raindrop = Raindrop(self)
        raindrop_height = raindrop.rect.height
        for raindrop in self.raindrops.sprites():
            if raindrop.rect.y == (self.screen_height + raindrop_height):
                raindrop.rect.y = 0 - raindrop_height
    
    def _drop_raindrop(self):
        """Move raindrop downside"""
        for raindrop in self.raindrops.sprites():
            raindrop.rect.y += 1
    
    def _update_raindrops(self):
        """
        Move raindrop downside. If raindrop dissapears, move it above screen
        """
        self._drop_raindrop()
        self._recreate_raindrop()
        
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.bg_color)
        self.raindrops.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    # Make a program instance, and run the game.
    main_program = Sky()
    main_program.run_game()
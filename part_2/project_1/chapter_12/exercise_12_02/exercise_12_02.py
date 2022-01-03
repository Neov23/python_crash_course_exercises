# Exercise 12-2

import sys

import pygame

from dimitris import Dimitris

class World:
    """Overall class to manage the program's World."""
    def __init__(self):
        pygame.init()

        """Initialize the World, and create some resources"""
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("exercise_12_02")
        self.bg_color = (100, 230, 230)
        self.dimitris = Dimitris(self)

        # Create sky and Dimitris on screen
        self.screen.fill(self.bg_color)
        self.dimitris.blitme()
        pygame.display.flip()
    
    def run_program(self):
        """Start main loop of program"""
        while True:
            self.quit_program()

    def quit_program(self):
        """Way to end program."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

main_program = World()
main_program.run_program()
# Exercise 12-1

import sys

import pygame

class World:
    """Overall class to manage the program's World."""
    def __init__(self):
        pygame.init()
        """Initialize the World, and create some resources"""
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("exercise_12_01")
        self.bg_color = (100, 230, 230)

        # Create sky on screen
        self.screen.fill(self.bg_color)
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

program = World()
program.run_program()
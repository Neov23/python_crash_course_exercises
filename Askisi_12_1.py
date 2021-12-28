# Άσκηση 12-1

import sys

import pygame

class World:
    """Overall class to manage the program's world."""
    def __init__(self):
        pygame.init()
        """Initialize the world, and create some resources"""
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Askisi_12_1")
        self.bg_color = (100, 230, 230)
    
    def run_program(self):
        """Start main loop of program"""
        while True:
            self.quit_program()
            self.update_screen()

    def quit_program(self):
        """Way to end program."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def update_screen(self):
        """Updating the screen"""
        self.screen.fill(self.bg_color)
        pygame.display.flip()

runner = World()
runner.run_program()
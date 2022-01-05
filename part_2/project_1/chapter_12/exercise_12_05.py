# Exercise 12-5

import sys

import pygame

class ShowKey:
    """Overall class to manage the program"""

    def __init__(self):
        """Program initials"""
        pygame.init()

        # Initialize screen
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("exercise_12_05")
        self.bg_color = (0, 0, 0)
    
    def run_game(self):
        """Start the main loop of the program"""
        while True:
            self.check_events()
            self.update_screen()
    
    def check_events(self):
        """Check keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)

    def update_screen(self):
        """Update screen each time the loop replays"""
        self.screen.fill(self.bg_color)
        pygame.display.flip()
    
if __name__ == '__main__':
    # Make a game instance and run the game.
    main_program = ShowKey()
    main_program.run_game()
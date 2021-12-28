import sys

import pygame

class ShowKey:
    """Overall class to manage the program"""

    def __init__(self):
        """Program initials"""
        pygame.init()

        self.screen = pygame.display.set_mode((1024, 768))
        pygame.display.set_caption("Showkey program for exercise 12-5")
        self.bg_color = (0, 0, 0)
    
    def run_game(self):
        """Start the main loop of the program"""
        while True:
            self.check_events()
            self.update_screen()
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._keydown_events(event)
    
    def _keydown_events(self, event):
        """Respond to keypresses"""
        print(event.key)
        
        if event.key == pygame.K_q:
            sys.exit()


    def update_screen(self):
        """Update screen each time the loop replays"""
        self.screen.fill(self.bg_color)
        pygame.display.flip()
    
if __name__ == '__main__':
    # Make a game instance and run the game.
    sk = ShowKey()
    sk.run_game()
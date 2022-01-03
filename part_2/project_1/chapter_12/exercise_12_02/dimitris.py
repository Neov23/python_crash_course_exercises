import pygame

class Dimitris:
    """A class to represent Dimitris"""
    def __init__(self, program):
        """Initialize Dimitris and get his starting position."""
        self.screen = program.screen
        self.screen_rect = program.screen.get_rect()

        # Load thomas image and get its rect
        self.image = pygame.image.load('dimitris.bmp')
        self.rect = self.image.get_rect()

        # Start each new thomas at the center of the screen
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw Dimitris at his current location."""
        self.screen.blit(self.image, self.rect)
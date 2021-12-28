import pygame

class Thomas:
    """A class to represent thomas"""
    def __init__(self, from_runner):
        """Initialize thomas and get his starting position."""
        self.screen = from_runner.screen
        self.screen_rect = from_runner.screen.get_rect()

        # Load thomas image and get its rect
        self.image = pygame.image.load('thomas_image.bmp')
        self.rect = self.image.get_rect()

        # Start each new thomas at the center of the screen
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw thomas at his current location."""
        self.screen.blit(self.image, self.rect)


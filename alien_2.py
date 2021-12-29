import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, rg):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = rg.screen

        # Load the alien image and set its rect.
        self.image = pygame.image.load('real_ufo.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien to the left."""
        self.x -= 0.02
        self.rect.x = self.x
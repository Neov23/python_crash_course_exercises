import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, program):
        """Initialize the alien and set its starting position"""
        super().__init__()

        # Load the alien image and set its rect.
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien to the left."""
        self.x -= 0.02
        self.rect.x = self.x
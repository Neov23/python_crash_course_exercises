import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the rocket."""
    def __init__(self, game):
        """Create a bullet object at the rocket's current position."""
        super().__init__()
        self.screen = game.screen
        self.color = (255, 0, 0)

        # Create a bullet rect and set initial position.
        self.rect = pygame.Rect(0, 0, 15, 4)
        self.rect.midright = game.rocket.rect.midright

    def update(self):
        """Move the bullet up the screen."""
        self.rect.x += 1

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """Initialize a bullet"""

    def __init__(self, main_program):
        """Initialize it's attributes"""
        super().__init__()

        self.screen = main_program.screen

        # Create a bullet rect and set its initial position
        self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.midright = main_program.rocket.rect.midright
        self.color = (255, 0, 0)

    def update(self):
        """Move the bullet to the right"""
        self.rect.x += 2
    
    def draw_bullet(self):
        """Draw bullet on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
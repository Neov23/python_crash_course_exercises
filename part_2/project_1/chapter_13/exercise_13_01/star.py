# class Star

import pygame

from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single star"""

    def __init__(self, program):
        """Initialize the star"""
        super().__init__()
        
        # Load the star image and set its rect attribute
        self.image = pygame.image.load('star.bmp')
        self.rect = self.image.get_rect()
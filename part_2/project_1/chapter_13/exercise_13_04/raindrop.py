# class Raindrop

import pygame

from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to represent a single raindrop"""

    def __init__(self, program):
        """Initialize the raindrop"""
        super().__init__()
        
        # Load the star image and set its rect attribute
        self.image = pygame.image.load('raindrop.bmp')
        self.rect = self.image.get_rect()
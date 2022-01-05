import pygame

class Rocket:
    """A class to manage the rocket."""

    def __init__(self, program):
        self.screen = program.screen
        self.screen_rect = program.screen.get_rect()

        # Load the rocket image and get its rect.
        self.image = pygame.image.load('rocket.bmp')
        self.rect = self.image.get_rect()

        # Rocket's initial position
        self.rect.midleft = self.screen_rect.midleft

        # Movement flags
        self.moving_up = False
        self.moving_down = False

        self.y = float(self.rect.y)

    def update(self):
        """Update the rocket's position based on the movement flags."""
        if self.moving_up and self.rect.top > 0:
            self.y -= 0.7
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 0.7
        self.rect.y = self.y
    
    def blitme(self):
        """Draw the rocket at its current location"""
        self.screen.blit(self.image, self.rect)
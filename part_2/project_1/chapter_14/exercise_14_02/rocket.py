import pygame

class Rocket:
    """Create a rocket"""

    def __init__(self, main_program):
        """Initialize rocket's rect and position."""
        self.screen = main_program.screen
        self.screen_rect = main_program.screen.get_rect()

        # Get it's image, create rect and initialize position
        self.image = pygame.image.load('rocket.bmp')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

        # Store rocket's position as a decimal value
        self.y = float(self.rect.y)

        # Movement flags
        self.move_up = False
        self.move_down = False

    def update(self):
        """Update rocket's position based on movement flags"""
        if self.move_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += 1
        if self.move_up and self.rect.top >= 0:
            self.y -= 1
        
        self.rect.y = self.y
    
    def blitme(self):
        """Draw the rocket at current position"""
        self.screen.blit(self.image, self.rect)
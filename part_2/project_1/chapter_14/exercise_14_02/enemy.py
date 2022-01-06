import pygame

class Enemy:
    """Create the enemy object"""

    def __init__(self, main_program):
        """Initialize its rect and position on screen"""
        self.screen = main_program.screen
        self.screen_rect = main_program.screen.get_rect()
        self.color = (100, 200, 255)

        # Create rect and set it's initial position
        self.rect = pygame.Rect(0, 0, 10, 30)
        self.rect.midright = self.screen_rect.midright

        # Store rect's position as a decimal value
        self.y = float(self.rect.y)

        # Set a flag to change direction when rect reaches the edge
        self.direction = 1

    def update(self):
        """Move the rect up and down the screen"""
        if self.rect.bottom >= self.screen_rect.bottom:
            self.direction = self.direction * -1
        if self.rect.top < 0:
            self.direction = self.direction * -1

        self.y += 0.4 * self.direction
        
        self.rect.y = self.y

    def draw_enemy(self):
        """Draw enemy on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
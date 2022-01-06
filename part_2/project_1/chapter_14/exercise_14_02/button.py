import pygame.font

class Button:
    """Create button"""

    def __init__(self, main_program, msg):
        """Initialize button attributes."""
        self.screen = main_program.screen
        self.screen_rect = main_program.screen.get_rect()

        # Set size and properties of button
        self.width, self.height = 300, 80
        self.button_color = (100, 100, 100)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 64)

        # Build button's rect and initialize its position
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Create message
        self._msg(msg)
    
    def _msg(self, msg):
        """Turn msg into rendered image and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color,
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw button then draw message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
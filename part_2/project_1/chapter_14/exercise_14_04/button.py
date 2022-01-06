import pygame.font

class Button:

    def __init__(self, ai_game, position):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        # Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (70, 140, 210)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = self.settings.screen_width // 2 - self.width // 2
        self.rect.y = self.height * 1.5 * position

        # Set difficulty. Each level raises speed by 20%
        self.settings.ship_speed * 1.2**position
        self.settings.bullet_speed * 1.2**position
        self.settings.alien_speed * 1.2**position
    
        # The button message needs to be prepped only once.
        self._prep_msg(position)

    def _prep_msg(self, position):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(f"Level {position}", True, 
            self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def set_difficulty(self, position):
        """Set difficulty. Each level raises speed by 20%"""
        self.settings.ship_speed *= 1.2**position
        self.settings.bullet_speed *= 1.2**position
        self.settings.alien_speed *= 1.2**position
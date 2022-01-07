class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10
        
        # How quickly the game speeds up
        self.speedup_scale = 1.2

        # Dynamic settings
        self.ship_speed = 0.7
        self.bullet_speed = 0.7
        self.alien_speed = 0.1

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def reset_settings(self):
        self.ship_speed = 0.7
        self.bullet_speed = 0.7
        self.alien_speed = 0.1
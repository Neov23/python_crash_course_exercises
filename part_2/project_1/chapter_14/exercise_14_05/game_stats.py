class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initalize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = 0
        self.load_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    
    def save_stats(self):
        filename = 'high_score.json'

        with open(filename, 'w') as f:
            f.write(str(self.high_score))
    
    def load_stats(self):
        try:
            filename = 'high_score.json'

            with open(filename) as f:
                loaded_score = f.read()
                self.high_score = int(loaded_score)
        except FileNotFoundError:
            pass
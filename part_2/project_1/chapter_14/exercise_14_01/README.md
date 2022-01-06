# Exercise 14-1 [(link)](exercise_14_01.py)

- **Highlight:**

```
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()

    def _start_game(self):
        """Start a new game"""
        self.stats.reset_stats()
        self.stats.game_active = True

        # Get rid of any remaining aliens and bullets.
        self.aliens.empty()
        self.bullets.empty()

        # Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.center_ship()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
    
    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        --snip--
        elif event.key == pygame.K_p:
            if not self.stats.game_active:
                self._start_game()
```

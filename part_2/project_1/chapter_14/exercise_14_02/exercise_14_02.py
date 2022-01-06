# Exercise 14-2

import sys

import pygame

from enemy import Enemy

from rocket import Rocket
from bullet import Bullet
from button import Button

class Game:
    """Initialize the game"""

    def __init__(self):
        pygame.init()

        # Screen settings
        self.screen = pygame.display.set_mode((1280, 960))
        pygame.display.set_caption("exercise_14_02")
        self.bg_color = (0, 0, 0)

        self.button = Button(self, "Start Game")
        self.rocket = Rocket(self)
        self.enemy = Enemy(self)
        self.bullets = pygame.sprite.Group()
        self.removed_bullets = 0

        # Flag to determine whether the game is active or not
        self.game_active = False

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.game_active:
                self.rocket.update()
                self.enemy.update()
                self._update_bullet()
                self.__end_game()
            self._update_screen()
    
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_UP:
            self.rocket.move_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.move_down = True
    
    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_UP:
            self.rocket.move_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.move_down = False
    
    def _initialize_game(self):
        """Start game. Initialize position and settings of all objects"""
        self.game_active = True

        # Initialize objects
        self.rocket.rect.midleft = self.rocket.screen_rect.midleft
        self.enemy.rect.midright = self.enemy.screen_rect.midright
        self.bullets.empty()
        self.removed_bullets = 0
    
    def _check_play_button(self, mouse_pos):
        press_start = self.button.rect.collidepoint(mouse_pos)
        if press_start and not self.game_active:
            self._initialize_game()
    
    def _fire_bullet(self):
        bullet = Bullet(self)
        self.bullets.add(bullet)

    def _removed_bullets(self):
        removed_bullets = 0
        for bullet in self.bullets.sprites():
            removed_bullets += 1

    def _update_bullet(self):
        """Update bullets position and remove off screen bullets"""
        self.bullets.update()
        screen_rect = self.screen.get_rect()

        # Get rid of off screen bullets and count removed bullets
        for bullet in self.bullets.copy():
            if bullet.rect.left >= screen_rect.right:
                self.removed_bullets += 1
                self.bullets.remove(bullet)
    
    def __end_game(self):
        """If bullet and enemy collide, end the game"""
        if pygame.sprite.spritecollideany(self.enemy, self.bullets):
            self.game_active = False
        if self.removed_bullets >= 3:
            self.game_active = False

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.rocket.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.enemy.draw_enemy()
        if not self.game_active:
            self.button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    # Make a program instance and run the game
    program = Game()
    program.run_game()
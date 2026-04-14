import pygame
from views import GameView


class GameController:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.view = GameView(screen)
        self.state = None
        self.game_state = "menu"  # menu, playing, game_over

    def draw(self):
        if self.game_state == "menu":
            self.menu_buttons = self.view.draw_menu()
        elif self.game_state == "playing":
            self.view.draw_field()
            ...

import pygame
from random import randint


class Colors:
    TOWER_FRONT_V1 = (128, 128, 128)
    TOWER_HEADER_V1 = (0, 0, 0)
    GOBLINS = (0, 255, 0)
    FIELD = (20, 160, 44)
    SAND = (238, 214, 175)  
    TOWER_FRONT_V2 = (160, 128, 160)
    TOWER_HEADER_V2 = (32, 0, 32)
    TOWER_FRONT_V3 = (192, 128, 192)
    TOWER_HEADER_V3 = (64, 0, 64)
    OGRES = (0, 255, 60)
    BIG_BOB = (255, 62, 255)
    MONEY = (255, 255, 0)
    TEXT = (0, 0, 0)
    BUTTON = (0, 0, 122)
    BUTTON_ACTIVE = (0, 0, 255)


class GameView:
    """Класс, отвечающий за отрисовку игры"""
    # Параметры для экрана игры
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    GRID_SIZE = 40
    GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
    GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

    # Параметры для поля
    STRIP_POSITIONS = [200, 400, 600]
    STRIP_WIDTH = 80

    SPEED = 10

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font_large = pygame.font.Font(None, 48)  # размер шрифтов
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)

    def draw_field(self):
        self.screen.fill(Colors.FIELD)

        for pos in self.STRIP_POSITIONS:
            left_edge = pos - self.STRIP_WIDTH
            pygame.draw.rect(self.screen, Colors.SAND, ################################# screen
                             left_edge, self.STRIP_WIDTH, self.SCREEN_HEIGHT)

    def draw_menu(self):
        self.draw_field()

        title = self.font_large.render("Tower Defense in the Middle Ages", True, Colors.TEXT)
        title_rect = title.get_rect(center=(400, 150))
        self.screen.blit(title, title_rect)

        subtitle = self.font_small.render("Win this game", True, Colors.TEXT)
        sub_rect = subtitle.get_rect(center=(400, 210))
        self.screen.blit(subtitle, sub_rect)

        buttons = {}
        y = 340

        for text, action in [("Start new game", "start"), ("Exit", 'exit')]:
            mouse_pos = pygame.mouse.get_pos()
            rect = pygame.Rect(300, y, 200, 50)
            color = Colors.BUTTON_ACTIVE if rect.collidepoint(mouse_pos) else Colors.BUTTON

            pygame.draw.rect(self.screen, color, rect, border_radius=12)
            pygame.draw.rect(self.screen, Colors.TEXT, rect, 2, border_radius=12)

            but_text = self.font_medium.render(text, True, Colors.TEXT)
            text_rect = but_text.get_rect(center=rect.center)
            self.screen.blit(but_text, text_rect)
            buttons[action] = rect
            y += 70

        return buttons

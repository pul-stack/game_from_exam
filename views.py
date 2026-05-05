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
    BUTTON = (160, 145, 150)
    BUTTON_ACTIVE = (0, 0, 255)


class GameView:
    """Класс, отвечающий за отрисовку игры"""
    # Параметры для экрана игры
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
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

        self.goblin_img = pygame.image.load("assets/images/jean-nicolas-racicot-goblin-vox1.jpg")
        self.money_img = pygame.image.load("assets/images/money.gif")
        self.tower_v1_img = pygame.image.load("assets/images/tower_v1.png")
        self.tower_v2_img = pygame.image.load("assets/images/tower_v2.png")
        self.tower_v3_img = pygame.image.load("assets/images/tower_v3.png")
        self.ogrch_img = pygame.image.load("assets/images/ogre_img.jpg")
        self.big_bob_img = pygame.image.load("assets/images/Big_Bob.png")

    def draw_field(self):
        self.screen.fill(Colors.FIELD)

        for pos in self.STRIP_POSITIONS:
            left_edge = pos - self.STRIP_WIDTH // 2
            rect = pygame.Rect(left_edge, 0, self.STRIP_WIDTH, self.SCREEN_HEIGHT)
            pygame.draw.rect(self.screen, Colors.SAND, rect) # м.б что-то поменять ------------------------

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
    
    def draw_panel(self):
        cols = 3
        start_x = 1
        start_y = 600

        pygame.draw.rect(self.screen, Colors.BUTTON, pygame.Rect(start_x, start_y, 798, 230), border_radius=15)

        icon_tower_v1 = pygame.transform.scale(self.tower_v1_img, (200, 170))
        self.screen.blit(icon_tower_v1, (40, 615))

        icon_tower_v2 = pygame.transform.scale(self.tower_v2_img, (200, 170))
        self.screen.blit(icon_tower_v2, (300, 615))

        icon_tower_v1 = pygame.transform.scale(self.tower_v1_img, (200, 170))
        self.screen.blit(icon_tower_v1, (560, 615))


    def draw_enemy(self, enemy):
        """Отрисовка врага"""
        if enemy.color == Colors.GOBLINS:  # Нужно поменять
            img = self.goblin_img
            size = (30, 30)
        elif enemy.color == Colors.OGRES:  # Тоже
            img = self.ogrch_img
            size = (40,40)
        elif enemy.color == Colors.BIG_BOB:  # Тоже
            img = self.big_bob_img
            size = (55, 55)
        else:
            return
        
        img = pygame.transform.scale(img, size)
        self.screen.blit(img, (enemy.x - size[0]//2, enemy.y - size[1]//2))
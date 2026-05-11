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
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 810
    GRID_SIZE = 40
    GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
    GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

    # Параметры для поля
    STRIP_POSITIONS = [200, 400, 600]  # Центры дорожек
    STRIP_WIDTH = 80  # Ширина

    SPEED = 60

    GRASS_CENTERS = [80, 300, 500, 720]  # Центры травы по x

    TOWER_CELLS_Y = [50, 200, 350, 500]  # Y-координаты верхних границ ячеек
    TOWER_WIDTH = 76
    TOWER_HEIGHT = 140

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font_large = pygame.font.Font(None, 48)  # Размер шрифтов
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)

        self.goblin_img = pygame.image.load("assets/images/jean-nicolas-racicot-goblin-vox1.png")
        self.money_img = pygame.image.load("assets/images/money.gif")
        self.tower_v1_img = pygame.image.load("assets/images/tower_v1.png")
        self.tower_v2_img = pygame.image.load("assets/images/tower_v2.png")
        self.tower_v3_img = pygame.image.load("assets/images/tower_v3.png")
        self.ogrch_img = pygame.image.load("assets/images/ogre_img.png")
        self.big_bob_img = pygame.image.load("assets/images/Big_Bob.png")

        # Иконки сделанные под размер панели
        self.tower_v1_icon = pygame.transform.scale(self.tower_v1_img, (180, 150))
        self.tower_v2_icon = pygame.transform.scale(self.tower_v2_img, (180, 150))
        self.tower_v3_icon = pygame.transform.scale(self.tower_v3_img, (180, 150))

        self.current_health = 200
        self.current_money = 150

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
    
    # Отрисовка всей панели
    def draw_panel(self):
        start_x = 1
        start_y = 600
        pygame.draw.rect(self.screen, Colors.BUTTON, pygame.Rect(start_x, start_y, 798, 230), border_radius=15)

        mouse_pos = pygame.mouse.get_pos()

        tower_data = [
            (self.tower_v1_icon, 40, "Tower V1", "100"),
            (self.tower_v2_icon, 300, "Tower V2", "240"),
            (self.tower_v3_icon, 560, "Tower V3", "600"),
        ]

        for icon, x, name, price in tower_data:

            # Иконка с размерами для проверки
            icon_rect = pygame.Rect(x, 615, 180, 150)
            self.screen.blit(icon, (x, 615))

            # Если мышь над иконкой
            if icon_rect.collidepoint(mouse_pos):
                s = pygame.Surface((180, 150))
                s.set_alpha(80)
                s.fill(Colors.BUTTON_ACTIVE)
                self.screen.blit(s, (x, 615))

            name_text = self.font_small.render(name, True, Colors.TEXT)
            self.screen.blit(name_text, (x + 10, 615 + 155))
            # Иконка + цена
            coin = pygame.transform.scale(self.money_img, (48, 48))
            self.screen.blit(coin, (x - 10, 615 + 160))
            price_text = self.font_small.render(price, True, Colors.TEXT)
            self.screen.blit(price_text, (x + 28, 615 + 175))

        # Отображение HP и золота (передаётся из контроллера)
        # Место — левый верхний угол панели
        hp_text = self.font_medium.render(f"HP: {self.current_health}", True, Colors.TEXT)
        money_text = self.font_medium.render(f"Gold: {self.current_money}", True, Colors.TEXT)
        self.screen.blit(hp_text, (25, 608))
        self.screen.blit(money_text, (25, 638))

        # Иконка монетки
        money_icon = pygame.transform.scale(self.money_img, (60, 60))
        self.screen.blit(money_icon, (-18, 620))

    # Возвращает rect для башни по индексам
    def get_tower_rect(self, grass_index, cell_index):
        x = self.GRASS_CENTERS[grass_index] - self.TOWER_WIDTH // 2  # Получаем левый край прямоугольника
        y = self.TOWER_CELLS_Y[cell_index]
        return pygame.Rect(x, y, self.TOWER_WIDTH, self.TOWER_HEIGHT)

    # Отрисовка установленной башни
    def draw_tower_on_field(self, tower):
        rect = self.get_tower_rect(tower.grass_index, tower.cell_index)
        
        # Выбираем картинку по типу башни
        from models import Tower_v1, Tower_v2, Tower_v3
        
        if isinstance(tower, Tower_v1):
            img = self.tower_v1_img
        elif isinstance(tower, Tower_v2):
            img = self.tower_v2_img
        elif isinstance(tower, Tower_v3):
            img = self.tower_v3_img
        else:
            img = self.tower_v1_img  # запасной вариант
        
        # Масштабируем под размер ячейки и рисуем
        img = pygame.transform.scale(img, (rect.width, rect.height))
        self.screen.blit(img, (rect.x, rect.y))  # Рисует картинку на экране в нужном месте 
        
        # Цена поверх картинки
        coin = pygame.transform.scale(self.money_img, (42, 42))
        self.screen.blit(coin, (rect.x - 23, rect.y - 10))
        price_text = self.font_small.render(f"{tower.price}", True, Colors.TEXT)   # Текст превращается в картинку с сглаженным текстом
        self.screen.blit(price_text, (rect.x + 5, rect.y + 5))  # Пишет текст в нужном месте

    # Подсветка ячейки (жёлтая - можно, красная - нельзя) и радиуса атаки башни
    def draw_tower_preview(self, grass_index, cell_index, can_place, range_radius=None):
        if grass_index is None or cell_index is None:  # Если мышь не над травой или не над ячейкой
            return
        
        rect = self.get_tower_rect(grass_index, cell_index)

        if range_radius:
            center_x = self.GRASS_CENTERS[grass_index]
            center_y = self.TOWER_CELLS_Y[cell_index] + self.TOWER_HEIGHT // 2

            s = pygame.Surface((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.SRCALPHA)
            pygame.draw.circle(s, (255, 255, 100, 40), (center_x, center_y), range_radius)
            self.screen.blit(s, (0, 0))

        # Подсветка ячейки
        s2 = pygame.Surface((rect.width, rect.height))
        s2.set_alpha(80)
        if can_place:
            s2.fill(Colors.MONEY)
        else:
            s2.fill((255, 80, 80))
        self.screen.blit(s2, (rect.x, rect.y))

        pygame.draw.rect(self.screen, Colors.TEXT, rect, 2, border_radius=8)

    def draw_projectile(self, proj):
        """Отрисовка снаряда с хвостом"""
        r, g, b = proj.color
        # Основной снаряд (яркая точка)
        pygame.draw.circle(self.screen, proj.color, (int(proj.x), int(proj.y)), 4)
        # Свечение вокруг снаряда
        s = pygame.Surface((12, 12), pygame.SRCALPHA)
        pygame.draw.circle(s, (r, g, b, 80), (6, 6), 6)
        self.screen.blit(s, (int(proj.x) - 6, int(proj.y) - 6))
        # Тонкая линия от башни до снаряда
        pygame.draw.line(self.screen, (r, g, b, 60),
                         (proj.start_x, proj.start_y),
                         (int(proj.x) , int(proj.y)), 1)

    def draw_enemy(self, enemy):
        """Отрисовка врага со способностью и без"""
        # Выбор картинки и размера по типу врага    
        if enemy.enemy_type == "Goblin":
            img = self.goblin_img
            size = (30, 30)
        elif enemy.enemy_type == "Ogre":
            img = self.ogrch_img
            size = (40,40)
        elif enemy.enemy_type == "Big Bob":
            img = self.big_bob_img
            size = (55, 55)
        else:
            return
        
        img = pygame.transform.scale(img, size)
        # Координаты левого верхнего угла картинки
        x = enemy.x - size[0] // 2  # Обновляется в реальном времени
        y = enemy.y - size[1] // 2

        # Проверка, есть ли у врага способность
        has_ability = enemy.color not in [Colors.GOBLINS, Colors.OGRES, Colors.BIG_BOB]

        if has_ability:
            # Рисуется цветная рамка
            rect = pygame.Rect(x - 3, y - 3, size[0] + 6, size[1] + 6)  # Прямоугльник чуть больше иконки enemy
            pygame.draw.rect(self.screen, enemy.color, rect, 2, border_radius=4)

            # Цветная полоска над врагом
            bar_width = size[0]
            bar_height = 5
            bar_x = x
            bar_y = y - 10
            pygame.draw.rect(self.screen, enemy.color, (bar_x, bar_y, bar_width, bar_height))
            pygame.draw.rect(self.screen, Colors.TEXT, (bar_x, bar_y, bar_width, bar_height), 1)
        
        # Рисуется сама картинка врага
        self.screen.blit(img, (x, y))

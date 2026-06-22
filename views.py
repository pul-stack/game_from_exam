from constants import (Colors, SCREEN_WIDTH, SCREEN_HEIGHT, STRIP_POSITIONS, STRIP_WIDTH, 
                       GRASS_CENTERS, TOWER_CELLS_Y, TOWER_WIDTH, TOWER_HEIGHT,
                       BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_X,
                       TOWER_ICON_WIDTH, TOWER_ICON_HEIGHT, TOWER_ICON_Y)
import pygame
from models import Tower_v1, Tower_v2, Tower_v3


class GameView:
    """Класс, отвечающий за отрисовку игры"""

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font_large = pygame.font.Font(None, 52)
        self.font_medium = pygame.font.Font(None, 40)
        self.font_small = pygame.font.Font(None, 28)

        self.goblin_img = pygame.image.load("assets/images/jean-nicolas-racicot-goblin-vox1.png")
        self.money_img = pygame.image.load("assets/images/money.gif")
        self.tower_v1_img = pygame.image.load("assets/images/tower_v1.png")
        self.tower_v2_img = pygame.image.load("assets/images/tower_v2.png")
        self.tower_v3_img = pygame.image.load("assets/images/tower_v3.png")
        self.ogrch_img = pygame.image.load("assets/images/ogre_img.png")
        self.big_bob_img = pygame.image.load("assets/images/Big_Bob.png")
        self.menu_bg = pygame.image.load("assets/images/menu_background.jpg")

        # Иконки сделанные под размер панели
        self.tower_v1_icon = pygame.transform.scale(self.tower_v1_img, (TOWER_ICON_WIDTH, TOWER_ICON_HEIGHT))
        self.tower_v2_icon = pygame.transform.scale(self.tower_v2_img, (TOWER_ICON_WIDTH, TOWER_ICON_HEIGHT))
        self.tower_v3_icon = pygame.transform.scale(self.tower_v3_img, (TOWER_ICON_WIDTH, TOWER_ICON_HEIGHT))

        self.menu_bg = pygame.transform.scale(self.menu_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Кадры взрыва
        self.explosions = []
        for i in range(1, 5):
            img = pygame.image.load(f"assets/images/{i}_cadr.png")
            img = pygame.transform.scale(img, (40, 40))
            self.explosions.append(img)

    def draw_field(self):
        self.screen.fill(Colors.FIELD)

        for pos in STRIP_POSITIONS:
            left_edge = pos - STRIP_WIDTH // 2  # Левый край дорожки
            rect = pygame.Rect(left_edge, 0, STRIP_WIDTH, SCREEN_HEIGHT)
            pygame.draw.rect(self.screen, Colors.SAND, rect)

    def draw_menu(self):
        self.screen.blit(self.menu_bg, (0, 0))

        title = self.font_large.render("Tower Defense in the Middle Ages", True, Colors.TEXT)
        title_rect = title.get_rect(center=(400, 100))
        self.screen.blit(title, title_rect)

        subtitle = self.font_small.render("Win this game", True, Colors.TEXT)
        sub_rect = subtitle.get_rect(center=(400, 160))
        self.screen.blit(subtitle, sub_rect)

        buttons = {}
        y = 440

        for text, action in [("Start new game", "start"), ("Settings", "settings"), ("Exit", "exit")]:
            mouse_pos = pygame.mouse.get_pos()
            rect = pygame.Rect(BUTTON_X, y, BUTTON_WIDTH, BUTTON_HEIGHT)
            color = Colors.BUTTON_ACTIVE if rect.collidepoint(mouse_pos) else Colors.BUTTON

            pygame.draw.rect(self.screen, color, rect, border_radius=12)  # Кнопка
            pygame.draw.rect(self.screen, Colors.TEXT, rect, 2, border_radius=12)  # Рамка вокруг кнопки

            # Текст внутри кнопки
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
            icon_rect = pygame.Rect(x, TOWER_ICON_Y, TOWER_ICON_WIDTH, TOWER_ICON_HEIGHT)
            self.screen.blit(icon, (x, TOWER_ICON_Y))

            # Если мышь над иконкой
            if icon_rect.collidepoint(mouse_pos):
                s = pygame.Surface((TOWER_ICON_WIDTH, TOWER_ICON_HEIGHT))
                s.set_alpha(80)
                s.fill(Colors.BUTTON_ACTIVE)
                self.screen.blit(s, (x, TOWER_ICON_Y))

            name_text = self.font_small.render(name, True, Colors.TEXT)
            self.screen.blit(name_text, (x + 10, TOWER_ICON_Y + 155))
            # Иконка + цена
            coin = pygame.transform.scale(self.money_img, (48, 48))
            self.screen.blit(coin, (x - 10, TOWER_ICON_Y + 160))
            price_text = self.font_small.render(price, True, Colors.TEXT)
            self.screen.blit(price_text, (x + 28, TOWER_ICON_Y + 175))

        # Отображение HP и золота (передаётся из контроллера)
        # Место — левый верхний угол панели
        hp_text = self.font_medium.render(f"HP: {self.current_health}", True, Colors.TEXT)
        money_text = self.font_medium.render(f"Gold: {self.current_money}", True, Colors.TEXT)
        self.screen.blit(hp_text, (25, TOWER_ICON_Y - 7))
        self.screen.blit(money_text, (25, TOWER_ICON_Y + 23))

        # Иконка монетки
        money_icon = pygame.transform.scale(self.money_img, (60, 60))
        self.screen.blit(money_icon, (-18, TOWER_ICON_Y + 5))

    def draw_settings(self):
        self.screen.blit(self.menu_bg, (0, 0))

        title = self.font_large.render("Difficulty", True, Colors.TEXT)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 150))
        self.screen.blit(title, title_rect)

        buttons = {}
        y = 340
        for text, action in [("Easy", "easy"), ("Medium", "medium"), ("Hard", "hard")]:
            mouse_pos = pygame.mouse.get_pos()
            rect = pygame.Rect(BUTTON_X, y, BUTTON_WIDTH, BUTTON_HEIGHT)
            color = Colors.BUTTON_ACTIVE if rect.collidepoint(mouse_pos) else Colors.BUTTON

            pygame.draw.rect(self.screen, color, rect, border_radius=12)
            pygame.draw.rect(self.screen, Colors.TEXT, rect, 2, border_radius=12)

            but_text = self.font_medium.render(text, True, Colors.TEXT)
            text_rect = but_text.get_rect(center=rect.center)
            self.screen.blit(but_text, text_rect)
            buttons[action] = rect
            y += 70

        return buttons

    # Возвращает rect для башни по индексам
    def get_tower_rect(self, grass_index, cell_index):
        x = GRASS_CENTERS[grass_index] - TOWER_WIDTH // 2  # Получаем левый край прямоугольника
        y = TOWER_CELLS_Y[cell_index]
        return pygame.Rect(x, y, TOWER_WIDTH, TOWER_HEIGHT)

    # Отрисовка установленной башни
    def draw_tower_on_field(self, tower):
        rect = self.get_tower_rect(tower.grass_index, tower.cell_index)

        # Выбираем картинку по типу башни
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

    # Подсветка ячейки (жёлтая - можно) и радиуса атаки башни
    def draw_tower_preview(self, grass_index, cell_index, can_place, range_radius=None):
        if grass_index is None or cell_index is None:  # Если мышь не над травой или не над ячейкой
            return

        rect = self.get_tower_rect(grass_index, cell_index)

        # Радиус атаки
        if range_radius:
            center_x = GRASS_CENTERS[grass_index]
            center_y = TOWER_CELLS_Y[cell_index] + TOWER_HEIGHT // 2

            s = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
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
        pygame.draw.circle(self.screen, proj.color, (int(proj.x), int(proj.y)), radius=4)

    def draw_enemy(self, enemy):
        """Отрисовка врага со способностью и без"""
        # Выбор картинки и размера по типу врага
        if enemy.enemy_type == "Goblin":
            img = self.goblin_img
            size = (30, 30)
        elif enemy.enemy_type == "Ogre":
            img = self.ogrch_img
            size = (40, 40)
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

    def draw_explosions(self, explosion):
        """Отрисовка взрыва"""
        img = self.explosions[explosion.cadr]
        self.screen.blit(img, (explosion.x - 20, explosion.y - 20))  # Чтобы сместить взрыв в центр снаряда

    def draw_game_over(self):
        "Экран поражения"
        # Полупрозрачный тёмный фон на весь экран
        s = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        s.fill((0, 0, 0, 180))
        self.screen.blit(s, (0, 0))

        go_text = self.font_large.render("GAME OVER", True, (255, 80, 80))
        go_rect = go_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(go_text, go_rect)

        # Подсказка
        help_text = self.font_small.render("Нажмите ESC, чтобы выйти из игры", True, Colors.TEXT)
        help_rect = help_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))
        self.screen.blit(help_text, help_rect)

    def draw_tower_menu(self, tower, pos):
        """Меню улучшения/продажи башни"""
        upgrade_rect = pygame.Rect(pos[0] - 50, pos[1]- 60, 100, 25)
        sell_rect = pygame.Rect(pos[0] - 50, pos[1] - 30, 100, 25)

        # Фон меню
        pygame.draw.rect(self.screen, Colors.BUTTON, upgrade_rect, border_radius=15)
        pygame.draw.rect(self.screen, Colors.BUTTON, sell_rect, border_radius=15)

        # Текст
        upg_text = self.font_small.render(f"Улучшить ({tower.upgrade_cost})", True, Colors.TEXT)
        sell_text = self.font_small.render(f"Продать ({tower.total_invested // 2})", True, Colors.TEXT)

        self.screen.blit(upg_text, (pos[0] - 51, pos[1] - 57))
        self.screen.blit(sell_text, (pos[0] - 40, pos[1] - 27))

        # Если 5 уровень - кнопка улусшения неактивна
        if tower.level >= 5:
            pygame.draw.rect(self.screen, (255, 80, 80), upgrade_rect, 2, border_radius=15)

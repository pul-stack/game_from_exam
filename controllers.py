import pygame
from views import GameView
from models import Goblins, Ogres, Big_Bob, Tower_v1, Tower_v2, Tower_v3
import random


class GameController:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.view = GameView(screen)
        self.state = None
        self.game_state = "menu"  # menu, playing, game_over
        self.money = 100
        self.health = 200

        # Мобы и их спавн
        self.enemies : list = []
        self.spawn_timer = 0
        self.spawn_delay = 120 # Каждый 2 секунды

        # Список башен, выбранныый тип, наведение
        self.towers : list = []
        self.selected_tower_type = None  # "v1", "v2", "v3" или None
        self.hovered_grass = None
        self.hovered_cell = None

    def update(self):
        """Обновление игры каждый кадр"""
        if self.game_state == "playing":
            self.spawn_timer += 1  # За 2 секунлы будет 120
            if self.spawn_timer >= self.spawn_delay:
                self.spawn_timer = 0
                self.spawn_enemy()

            # Движение мобов
            for enemy in self.enemies[:]:
                enemy.y += enemy.speed / 60

                if enemy.y >= 581:
                    self.health -= enemy.damage  # Надо сделать формулу какую-то
                    self.enemies.remove(enemy)

                    if self.health <= 0:  # Где отображается hp?
                        self.health = 0
                        self.game_state = "game_over"

            # Обновление наведения мыши
            self.update_hover()

    # Определение над какой ячейкой мышь
    def update_hover(self):
        mouse_pos = pygame.mouse.get_pos()

        if mouse_pos[1] >= 600:
            self.hovered_grass = None  # Индекс линии травы
            self.hovered_cell = None  # Индекс ячейки по вертикали
            return

        self.hovered_grass = None  # Ищем линию травы
        for i, center in enumerate(GameView.GRASS_CENTERS):
            if abs(mouse_pos[0] - center) < GameView.TOWER_WIDTH // 2 + 10:
                self.hovered_grass = i
                break

        self.hovered_cell = None  # # Ищем ячейку по вертикали
        if self.hovered_grass is not None:  # Если мышь над травой
            for i, cell_y in enumerate(GameView.TOWER_CELLS_Y):
                if cell_y <= mouse_pos[1] < cell_y + GameView.TOWER_HEIGHT:
                    self.hovered_cell = i
                    break

    # Проверка занятости ячейки
    def free_cell(self, grass_index, cell_index):
        for tower in self.towers:
            if tower.grass_index == grass_index and tower.cell_index == cell_index:
                return True
        return False

    def spawn_enemy(self):
        """Создаёт случайного моба на любой из дорожек"""
        enemy_type = random.choices(
            [Goblins, Ogres, Big_Bob],
            weights=[75, 15, 10]
        )[0]

        enemy = enemy_type()  # Создаётся рандомный юнит

        strip = random.choice(GameView.STRIP_POSITIONS)  
        enemy.x = strip + random.randint(-20, 20)
        enemy.y = -40

        self.enemies.append(enemy)

    def draw(self):
        if self.game_state == "menu":
            self.menu_buttons = self.view.draw_menu()
        elif self.game_state == "playing":
            self.view.draw_field()

            self.view.current_health = self.health
            self.view.current_money = self.money

            self.view.draw_panel()

            # Подсветка при перетаскивании
            if self.selected_tower_type and self.hovered_grass is not None and self.hovered_cell is not None:
                can_place = not self.free_cell(self.hovered_grass, self.hovered_cell)
                self.view.draw_tower_preview(self.hovered_grass, self.hovered_cell, can_place)

            # Отрисовка установленных башен
            for tower in self.towers:
                self.view.draw_tower_on_field(tower)

            # Отрисовка юнитов
            for enemy in self.enemies:
                self.view.draw_enemy(enemy)

    def work_event(self, event):  # handle_event
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if self.game_state == "menu":
                buttons = self.view.draw_menu()
                if buttons.get("start") and buttons["start"].collidepoint(pos):
                    self.start_new_game()
                elif buttons.get("exit") and buttons["exit"].collidepoint(pos):
                    return False

            elif self.game_state == "playing":
                # Клик по панели — выбор башни
                if pos[1] >= 600:
                    if 40 <= pos[0] <= 220:
                        self.selected_tower_type = "v1"
                    elif 300 <= pos[0] <= 480:
                        self.selected_tower_type = "v2"
                    elif 560 <= pos[0] <= 740:
                        self.selected_tower_type = "v3"

                # Клик по полю — установка башни
                elif self.selected_tower_type and self.hovered_grass is not None and self.hovered_cell is not None:
                    if not self.free_cell(self.hovered_grass, self.hovered_cell):
                        self.place_tower(self.hovered_grass, self.hovered_cell)

        return True

    # Установка башни
    def place_tower(self, grass_index, cell_index):
        if self.selected_tower_type == "v1":
            tower = Tower_v1()
        elif self.selected_tower_type == "v2":
            tower = Tower_v2()
        elif self.selected_tower_type == "v3":
            tower = Tower_v3()
        else:
            return

        if self.money < tower.price:
            return

        self.money -= tower.price
        tower.grass_index = grass_index
        tower.cell_index = cell_index
        self.towers.append(tower)
        self.selected_tower_type = None

    def start_new_game(self):
        self.game_state = "playing"
        self.money = 100
        self.health = 200
        self.enemies = []
        self.towers = []
        self.selected_tower_type = None
        self.hovered_grass = None
        self.hovered_cell = None
        self.spawn_timer = 0

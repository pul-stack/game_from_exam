import pygame
from views import GameView
from models import Goblins, Ogres, Big_Bob
import random


class GameController:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.view = GameView(screen)
        self.state = None
        self.game_state = "menu"  # menu, playing, game_over
        self.money = 100
        self.health = 200

        self.enemies : list = []
        self.spawn_timer = 0
        self.spawn_delay = 120 # Каждый 2 секунды

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
            self.view.draw_panel()

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

            elif self.game_state == "playing":  # Будет установка башен
                pass

        return True
    
    def start_new_game(self):
        """Начинает новую игру"""
        self.game_state = "playing"
        self.money = 100
        self.health = 200
        self.enemies = []
        self.spawn_tower = 0
                    
    # def damage_base(self):
    #     damage = 
    #     new_health_base = self.health - 
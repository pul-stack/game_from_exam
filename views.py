import pygame
from random import randint


class Colors:
    TOWER_FRONT_V1 = (128, 128, 128)
    TOWER_HEADER_V1 = (0, 0, 0)
    GOBLINS = (0, 255, 0)
    FIELD = (20, 255, 44)
    TOWER_FRONT_V2 = (160, 128, 160)
    TOWER_HEADER_V2 = (32, 0, 32)
    TOWER_FRONT_V3 = (192, 128, 192)
    TOWER_HEADER_V3 = (64, 0, 64)
    OGRES = (0, 255, 60)
    BIG_BOB = (255, 62, 255)
    MONEY = (255, 255, 0)


class GameView:
    """"""
    SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
    GRID_SIZE = 40
    GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
    GRID_HEIGHT = SCREEN_WIDTH // GRID_SIZE

    SPEED = 10

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    pygame.display.set_caption('Tower Defense in the Middle Ages')


class Abilities:
    """Класс способностей для персонажей"""
    strong = {"health": 1.3,
             "damage": 1.3,
             "COLOR": (255, 0, 0),
             }

    fast = {"speed": 1.4,
            "COLOR": (0, 0, 255),
            }

    monetary = {"give_money": 1.4,
                "color": (255, 255, 0),
                }

    chance_strong = chance_fast = 0.1
    chance_monetary = 0.15

    def get_ability(self):
        get_monetary, get_strong, get_fast = 0, 1, 2

        if randint(1, 100) <= self.chance_monetary:
            return get_monetary
        elif randint(1, 100) <= self.chance_strong:
            return get_strong
        elif randint(1, 100) <= self.chance_fast:
            return get_fast


class Characters:
    """Класс для переопределения персонажей"""

    def __int__(self, health=None, damage=None, speed=None, lines=None, ability=None, give_money=None):
        self.health = 100
        self.damage = 10
        self.speed = GameView.SPEED
        self.lines = random.randint(1, 3)
        self.ability = Abilities.get_ability()
        self.give_money = 20

        


def main():
    """Основная функция запуска игры"""
    pygame.init()

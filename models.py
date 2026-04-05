import pygame
from random import randint


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
        get_monetary, get_strong, get_fast = "monetary", "strong", "fast"

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
        self.lines = randint(1, 3)
        self.ability = Abilities.get_ability()
        self.give_money = 20

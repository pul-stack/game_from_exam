import pygame
from random import randint
from views import GameView

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

    def __init__(self, health=100, damage=10, speed=GameView.SPEED, lines=None, ability=Abilities.get_ability(), give_money=20):
        self.health = health
        self.damage = damage
        self.speed = speed
        self.lines = lines if lines is not None else randint(1, 3)
        if ability is None:
            ab = Abilities()
            self.ability = ab.get_ability()
        else:
            self.ability = ability
        self.give_money = give_money

        def draw():
            pass


class Tower_v1(Characters):
    def __init__(self):
        super().__init__()

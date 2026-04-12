import pygame
from random import randint
from views import GameView, Colors

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

    @staticmethod
    def get_ability():
        get_monetary, get_strong, get_fast = "monetary", "strong", "fast"

        if randint(1, 100) <= Abilities.chance_monetary * 100:
            return get_monetary
        elif randint(1, 100) <= Abilities.chance_strong * 100:
            return get_strong
        elif randint(1, 100) <= Abilities.chance_fast * 100:
            return get_fast


class Characters:
    """Класс для переопределения персонажей"""

    def __init__(self, health=None, damage=None, speed=GameView.SPEED, lines=None, ability=Abilities.get_ability(), give_money=None, colors=None):
        self.health = health
        self.damage = damage
        self.speed = speed
        self.give_money = give_money
        self.colors = colors

        self.lines = lines if lines is not None else randint(1, 3)
        if ability is None:
            ab = Abilities()
            self.ability = ab.get_ability()
        else:
            self.ability = ability

        def draw(self, screen, x, y):
            """Отрисовка персонажа"""
            pass

        def edit_possition(self, screen, speed, x, y):
            pass

        def get_damage(self, screen, health):
            pass


class Towers:
    """Класс для переопределения башен"""

    def ___init__(self, health=None, damage=None, speed=GameView.SPEED, front_color=None, header_color=None):
        self.health = health
        self.damage = damage
        self.speed = speed
        self.front_color= front_color
        self.header_color = header_color

    def draw(self, screen, x, y):
        """Отрисовка башни"""
        pass


class Tower_v1(Towers):
    """Башня первой версии"""
    def __init__(self):
        super().__init__(
            health=200,
            damage=30,
            speed=10,
            front_color=Colors.TOWER_FRONT_V1,
            header_color=Colors.TOWER_HEADER_V1
            )


class Goblins(Characters):
    """Класс для гоблинов"""
    def __init__(self):
        super().__init__(
            health=70,
            damage=14,
            speed=10,
            lines=None,
            ability=None,
            give_money=20,
            color=Colors.GOBLINS
        )


class Tower_v2(Towers):
    """Башня второй версии"""
    def __init__(self):
        super().__init__(
            health=350,
            damage=53,
            speed=10,
            front_color=Colors.TOWER_FRONT_V2,
            header_color=Colors.TOWER_HEADER_V2
        )


class Tower_v3(Towers):
    """Башня третьей версии"""
    def __init__(self):
        super().__init__(
            health=500,
            damage=80,
            speed=10,
            front_color=Colors.TOWER_FRONT_V3,
            header_color=Colors.TOWER_HEADER_V3
        )


class Ogres(Characters):
    
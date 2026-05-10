import pygame
import random
from views import GameView, Colors

class Abilities:
    """Класс способностей для врагов"""
    abilities = {  # Сразу с шансом
        "strong":   {"health": 1.3, "damage": 1.3, "chance": 10, "color": (255, 100, 100)},
        "fast":     {"speed": 1.4, "chance": 10, "color": (100, 100, 255)},
        "monetary": {"give_money": 1.4, "chance": 15, "color": (255, 255, 100)},
    }

    @staticmethod
    def get_ability(enemy):
        "Случайная способность к врагу при спавне"
        names = list(Abilities.abilities.keys())
        chances = [Abilities.abilities[n]['chance'] for n in names]
        names.append(None)
        chances.append(100 - sum(chances))  # Шанс, что не будет способности

        name = random.choices(names, weights=chances, k=1)[0]
        if name is None:
            return
        
        stats = Abilities.abilities[name]
        if "strong" in stats:
            enemy.strong = int(enemy.strong * stats["strong"])
        if "health" in stats:
            enemy.health = int(enemy.health * stats["health"])
        if "speed" in stats:
            enemy.speed = int(enemy.speed * stats["speed"])
        if "give_money" in stats:
            enemy.give_money = int(enemy.give_money * stats["give_money"])
        if "color" in stats:
            enemy.color = stats["color"]

class Characters:
    """Класс для переопределения персонажей"""

    def __init__(self, health=None, damage=None, speed=GameView.SPEED, lines=None, ability=None, give_money=None, color=None):
        self.health = health
        self.damage = damage
        self.speed = speed if speed is not None else GameView.SPEED
        self.give_money = give_money
        self.color = color

        self.lines = lines if lines is not None else random.randint(1, 3)

    def draw(self, screen, x, y):
        """Отрисовка персонажа"""
        pass

    def update_position(self): 
        """Движение вниз по дорожке"""
        if self.y < 600:
            self.y += self.speed / 60

    def get_damage(self, screen, health):
        """Получение урона"""
        pass


class Towers:
    """Класс для переопределения башен"""

    def __init__(self, health=None, damage=None, speed=GameView.SPEED, front_color=None, header_color=None, price=None):
        self.health = health
        self.damage = damage
        self.speed = speed or GameView.SPEED
        self.front_color = front_color
        self.header_color = header_color
        self.price = price

        self.attack_timer = 0
        self.attack_speed = 60


    def draw(self, screen, x, y):
        """Отрисовка башни"""
        pass


class Tower_v1(Towers):
    """Башня первой версии"""
    def __init__(self):
        super().__init__(
            damage=30,
            speed=10,
            front_color=Colors.TOWER_FRONT_V1,
            header_color=Colors.TOWER_HEADER_V1,
            price=100
            )


class Goblins(Characters):
    """Класс для Гоблинов"""
    def __init__(self):
        super().__init__(
            health=70,
            damage=14,
            speed=23,
            lines=None,
            ability=None,
            give_money=20,
            color=Colors.GOBLINS
        )


class Tower_v2(Towers):
    """Башня второй версии"""
    def __init__(self):
        super().__init__(
            damage=54,
            speed=10,
            front_color=Colors.TOWER_FRONT_V2,
            header_color=Colors.TOWER_HEADER_V2,
            price=240
        )


class Tower_v3(Towers):
    """Башня третьей версии"""
    def __init__(self):
        super().__init__(
            damage=80,
            speed=10,
            front_color=Colors.TOWER_FRONT_V3,
            header_color=Colors.TOWER_HEADER_V3,
            price=600
        )


class Ogres(Characters):
    """Класс для Огров"""
    def __init__(self):
        super().__init__(
            health=140,
            damage=28,
            speed=18,
            lines=None,
            ability=None,
            give_money=50,
            color=Colors.OGRES
        )


class Big_Bob(Characters):
    """ Класс для Биг-Боба"""
    def __init__(self):
        super().__init__(
            health=800,
            damage=80,
            speed=14,
            lines=None,
            ability=None,
            give_money=200,
            color=Colors.BIG_BOB
        )

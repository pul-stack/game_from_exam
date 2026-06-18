import random
from views import Colors


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

    def __init__(self, health=None, damage=None, speed=60, lines=None, ability=None, give_money=None, color=None):
        self.health = health
        self.damage = damage
        self.speed = speed if speed is not None else 60
        self.give_money = give_money
        self.color = color

        self.enemy_type = None  # "Goblin", "Ogre", "Big Bob"

        self.lines = lines if lines is not None else random.randint(1, 3)


class Towers:
    """Класс для переопределения башен"""

    def __init__(self, health=None, damage=None, speed=60, front_color=None, header_color=None, price=None, attack_range=120):
        self.health = health
        self.damage = damage
        self.speed = speed or 60
        self.front_color = front_color
        self.header_color = header_color
        self.price = price

        self.attack_range = attack_range
        self.attack_timer = 0
        self.attack_speed = 60

        self.level = 1
        self.base_damage = damage if damage else 0
        self.base_range = attack_range
        self.total_invested = price if price else 0  # Общая вложенная сумма


class Missile:
    """Снаряд башни, летящий к врагу"""
    def __init__(self, x, y, target, damage, speed=6, color=(255, 255, 100)):
        self.x = x
        self.y = y
        self.target = target
        self.damage = damage
        self.speed = speed
        self.alive = True  # Жив ли снаряд
        self.color = color
        # Начальные положения координат
        self.start_x = x
        self.start_y = y

    def update(self):
        """Снаряд движется к цели и наносит ей урон"""
        # Если цель раньше умерла, то снаряд исчезает
        if not self.target or self.target.health <= 0:
            self.alive = False
            return

        # Вектор к цели
        dx = self.target.x - self.x
        dy = self.target.y - self.y
        dist = (dx**2 + dy**2) ** 0.5

        if dist < self.speed:
            # Снаряд достиг цели
            self.target.health -= self.damage
            self.alive = False
        else:
            # Движение к цели
            self.x += dx / dist * self.speed
            self.y += dy / dist * self.speed


class Tower_v1(Towers):
    """Башня первой версии"""
    def __init__(self):
        super().__init__(
            damage=30,
            speed=10,
            front_color=Colors.TOWER_FRONT_V1,
            header_color=Colors.TOWER_HEADER_V1,
            price=100,
            attack_range=200
        )
        self.upgrade_cost = 50


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
        self.enemy_type = "Goblin"


class Tower_v2(Towers):
    """Башня второй версии"""
    def __init__(self):
        super().__init__(
            damage=54,
            speed=10,
            front_color=Colors.TOWER_FRONT_V2,
            header_color=Colors.TOWER_HEADER_V2,
            price=240,
            attack_range=260
        )
        self.upgrade_cost = 100


class Tower_v3(Towers):
    """Башня третьей версии"""
    def __init__(self):
        super().__init__(
            damage=80,
            speed=10,
            front_color=Colors.TOWER_FRONT_V3,
            header_color=Colors.TOWER_HEADER_V3,
            price=600,
            attack_range=330
        )
        self.upgrade_cost = 250

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
        self.enemy_type = "Ogre"


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
        self.enemy_type = "Big Bob"


class Explosion:
    """Взрыв при попадании снаряда"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cadr = 0
        self.timer = 0
        self.alive = True

    def update(self):
        self.timer += 1
        if self.timer >= 5:
            self.timer = 0
            self.cadr += 1
            if self.cadr >= 4:
                self.alive = False

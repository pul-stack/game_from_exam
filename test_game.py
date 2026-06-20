import pygame
from controllers import GameController
from models import Tower_v1, Tower_v2, Tower_v3, Goblins, Ogres, Big_Bob, Abilities, Missile, Explosion
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


pygame.init()
screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
gamecon = GameController(screen)


# ---Тесты для проверки занятости ячеек---

def test_is_cell_occupied_empty():
    """Пустая ячейка - не занята"""
    gamecon.towers = []
    assert gamecon.is_cell_occupied(1, 2) == False


def test_is_cell_occupied_occupied():
    """Ячейка занята - занята"""
    tower = Tower_v1()
    tower.grass_index = 1
    tower.cell_index = 2
    gamecon.towers = [tower]
    assert gamecon.is_cell_occupied(1, 2) == True


def test_is_cell_occupied_other_cell():
    """Друшая ячейка - не занята"""
    tower = Tower_v1()
    tower.grass_index = 1
    tower.cell_index = 2
    gamecon.towers = [tower]
    assert gamecon.is_cell_occupied(1, 0) == False


# ---Тесты для башен---

def test_tower_v1_creation():
    """Создание башни V1 с правильными параметрами"""
    tower = Tower_v1()
    assert tower.damage == 30
    assert tower.price == 100
    assert tower.attack_range == 200
    assert tower.level == 1
    assert tower.upgrade_cost == 50


def test_tower_v2_creation():
    """Создание башни V2 с правильными параметрами"""
    tower = Tower_v2()
    assert tower.damage == 54
    assert tower.price == 240
    assert tower.attack_range == 260
    assert tower.level == 1
    assert tower.upgrade_cost == 100


def test_tower_v3_creation():
    """Создание башни V3 с правильными параметрами"""
    tower = Tower_v3()
    assert tower.damage == 80
    assert tower.price == 600
    assert tower.attack_range == 330
    assert tower.level == 1
    assert tower.upgrade_cost == 250


# --- Тесты для врагов ---

def test_goblin_creation():
    """Создание гоблина с правильными параметрами"""
    enemy = Goblins()
    assert enemy.health == 70
    assert enemy.damage == 14
    assert enemy.speed == 23
    assert enemy.give_money == 20
    assert enemy.enemy_type == "Goblin"


def test_ogre_creation():
    """Создание огра с правильными параметрами"""
    enemy = Ogres()
    assert enemy.health == 140
    assert enemy.damage == 28
    assert enemy.speed == 18
    assert enemy.give_money == 50
    assert enemy.enemy_type == "Ogre"


def test_big_bob_creation():
    """Создание Биг Боба с правильными параметрами"""
    enemy = Big_Bob()
    assert enemy.health == 800
    assert enemy.damage == 80
    assert enemy.speed == 14
    assert enemy.give_money == 200
    assert enemy.enemy_type == "Big Bob"


# --- Тесты для системы способностей ---

def test_ability_strong():
    """Способность Strong увеличивает HP и урон"""
    goblin = Goblins()
    start_hp = goblin.health
    start_dmg = goblin.damage

    # Применяем способность Strong
    goblin.health = int(goblin.health * 1.3)
    goblin.damage = int(goblin.damage * 1.3)
    goblin.color = (255, 100, 100)

    assert goblin.health > start_hp
    assert goblin.damage > start_dmg
    assert goblin.color == (255, 100, 100)


def test_ability_fast():
    """Способность Fast увеличиает скорость"""
    goblin = Goblins()
    start_speed = goblin.speed

    # Применяем способность Fast
    goblin.speed = int(goblin.speed * 1.4)
    goblin.color = (100, 100, 255)

    assert goblin.speed > start_speed
    assert goblin.color == (100, 100, 255)


def test_ability_monetary():
    """Способность Monetary увеличивает награду за enemy"""
    goblin = Goblins()
    start_money = goblin.give_money

    goblin.give_money = int(goblin.give_money * 1.4)
    goblin.color = (255, 255, 100)

    assert goblin.give_money > start_money
    assert goblin.color == (255, 255, 100)


# --- Тесты для снарядов ---

def test_missile_creation():
    """Создание снаряда с правильными параметрами"""
    target = Goblins()
    target.x = 100
    target.y = 100

    missile = Missile(0, 0, target, damage=30, speed=6, color=(255, 255, 100))

    assert missile.x == 0
    assert missile.y == 0
    assert missile.target == target
    assert missile.damage == 30
    assert missile.speed == 6
    assert missile.alive == True
    assert missile.color == (255, 255, 100)


def test_missile_movement():
    """Снаряд движется к цели"""
    target = Goblins()
    target.x = 100
    target.y = 0

    missile = Missile(0, 0, target, damage=30, speed=10)
    start_x = missile.x
    start_y = missile.y

    missile.update()

    # Снаряд должен приблизиться к цели
    assert missile.x > start_x or missile.y > start_y
    assert missile.alive == True


def test_missile_hit_target():
    """Снаряд наносит урон цели при попадании"""
    target = Goblins()
    target.x = 5
    target.y = 0
    target.health = 70

    missile = Missile(0, 0, target, damage=30, speed=10)
    start_health = target.health

    missile.update()

    # Снаряд должен достичь цели и нанести урон
    assert target.health < start_health
    assert missile.alive == False


def test_missile_disappear_without_target():
    """Снаряд исчезает, если target побеждён"""
    target = Goblins()
    target.x = 100
    target.y = 100
    target.health = 0  # target побеждён

    missile = Missile(0, 0, target, damage=30, speed=6)
    missile.update()

    assert missile.alive == False


# --- Тесты для взрывов ---

def test_explosion_creation():
    """Создание взрыва с правильными параметрами"""
    explosion = Explosion(100, 200)

    assert explosion.x == 100
    assert explosion.y == 200
    assert explosion.cadr == 0
    assert explosion.timer == 0
    assert explosion.alive == True


def test_explosion_animation():
    """Взрыв анимируется и исчезает"""
    explosion = Explosion(100, 200)

    # Обновляется взрыв несколько раз
    for _ in range(20):
        explosion.update()

    # Взрыв должен завершиться
    assert explosion.alive == False
    assert explosion.cadr >= 4


# --- Запуск тестов ---

if __name__ == "__main__":
    test_is_cell_occupied_empty()
    test_is_cell_occupied_occupied()
    test_is_cell_occupied_other_cell()

    test_tower_v1_creation()
    test_tower_v2_creation()
    test_tower_v3_creation()

    test_goblin_creation()
    test_ogre_creation()
    test_big_bob_creation()

    test_ability_strong()
    test_ability_fast()
    test_ability_monetary()

    test_missile_creation()
    test_missile_movement()
    test_missile_hit_target()
    test_missile_disappear_without_target()

    test_explosion_creation()
    test_explosion_animation()

    print("Все тесты пройдены!")
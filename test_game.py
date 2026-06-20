import pygame
from controllers import GameController
from models import Tower_v1, Tower_v2, Tower_v3, Goblins, Ogres, Big_Bob, Abilities, Missile, Explosion
from constants import SCREEN_WIDTHб, SCREEN_HEIGHT


pygame.init()
screen = pygame.Surface(SCREEN_WIDTH, SCREEN_HEIGHT)
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
    """Создание башни V3 с правильными параметрами"""
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
    assert enemy.spped == 23
    assert enemy.give_money == 20
    assert enemy.enemy_type == "Goblin"


def test_ogre_creation():
    """Создание гоблина с правильными параметрами"""
    enemy = Ogres()
    assert enemy.health == 140
    assert enemy.damage == 28
    assert enemy.spped == 18
    assert enemy.give_money == 50
    assert enemy.enemy_type == "Ogre"


def test_big_bob_creation():
    """Создание гоблина с правильными параметрами"""
    enemy = Big_Bob()
    assert enemy.health == 800
    assert enemy.damage == 80
    assert enemy.spped == 14
    assert enemy.give_money == 200
    assert enemy.enemy_type == "Big Bob"


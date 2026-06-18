import pygame
from controllers import GameController
from models import Tower_v1

pygame.init()

screen = pygame.Surface((800, 810))
gc = GameController(screen)


def test_free_cell_empty():
    """Пустая ячейка — свободна"""
    gc.towers = []
    assert gc.free_cell(1, 2) == False


def test_free_cell_occupied():
    """Ячейка занята — занята"""
    tower = Tower_v1()
    tower.grass_index = 1
    tower.cell_index = 2
    gc.towers = [tower]
    assert gc.free_cell(1, 2) == True


def test_free_cell_other_cell():
    """Другая ячейка — свободна"""
    tower = Tower_v1()
    tower.grass_index = 1
    tower.cell_index = 2
    gc.towers = [tower]
    assert gc.free_cell(1, 0) == False

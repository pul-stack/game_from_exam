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

import pygame
from views import GameView

def main():
    """Функция, управляющая работой всей игры"""
    pygame.init()

    screen = pygame.display.set_mode((GameView.SCREEN_WIDTH, GameView.SCREEN_HEIGHT), 0, 32)
    pygame.display.set_caption('Tower Defense in the Middle Ages')
    clock = pygame.time.Clock()
    
    running = True
    while running:
        
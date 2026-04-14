import pygame
from views import GameView
from controllers import GameController
import sys


def main():
    """Функция, управляющая работой всей игры"""
    pygame.init()

    screen = pygame.display.set_mode((GameView.SCREEN_WIDTH, GameView.SCREEN_HEIGHT), 0, 32)
    pygame.display.set_caption('Tower Defense in the Middle Ages')
    clock = pygame.time.Clock()

    game_controller = GameController(screen)

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            ...

        game_controller.draw()

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

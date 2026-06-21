import pygame
from controllers import GameController
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    """Функция, управляющая работой всей игры"""
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    pygame.display.set_caption('Tower Defense in the Middle Ages')
    clock = pygame.time.Clock()  # таймер для контроля ФПС

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

            result = game_controller.work_event(event)
            if result is False:  # is - идентичностью объектов (ссылаются ли они на что-то общее (один и тот же объект в памяти))
                running = False

        game_controller.update()  # Вызывается 60 раз в секунду
        # game_controller
        game_controller.draw()
        # Обновление экрана (обязательная строка)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

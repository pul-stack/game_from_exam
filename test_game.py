import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Зелёное поле с песочными линиями")
clock = pygame.time.Clock()
running = True

# ЦВЕТА
GREEN_FIELD = (20, 255, 44)      # Зелёное поле
SAND_COLOR = (238, 214, 175)     # Песочный цвет

# Размеры
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Ширина каждой песочной полосы
STRIP_WIDTH = 80

# Позиции полос (равномерно распределены)
# 800 / 4 = 200 между центрами
STRIP_POSITIONS = [160, 360, 560]  # Центры полос

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Заливка зелёным
    screen.fill(GREEN_FIELD)
    
    # Рисуем 3 широкие песочные полосы
    for pos in STRIP_POSITIONS:
        # Вычисляем левый край полосы
        left_edge = pos - STRIP_WIDTH // 2
        pygame.draw.rect(screen, SAND_COLOR, 
                        (left_edge, 0, STRIP_WIDTH, SCREEN_HEIGHT))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
#  Цвета
class Colors:
    TOWER_FRONT_V1 = (128, 128, 128)
    TOWER_HEADER_V1 = (0, 0, 0)
    GOBLINS = (0, 255, 0)
    FIELD = (20, 160, 44)
    SAND = (238, 214, 175)
    TOWER_FRONT_V2 = (160, 128, 160)
    TOWER_HEADER_V2 = (32, 0, 32)
    TOWER_FRONT_V3 = (192, 128, 192)
    TOWER_HEADER_V3 = (64, 0, 64)
    OGRES = (0, 255, 60)
    BIG_BOB = (255, 62, 255)
    MONEY = (255, 255, 0)
    TEXT = (0, 0, 0)
    BUTTON = (160, 145, 150)
    BUTTON_ACTIVE = (0, 0, 255)


# Размеры экрана и поля
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 810

STRIP_POSITIONS = [200, 400, 600]  # Центры дорожек
STRIP_WIDTH = 80                   # Ширина дорожек

GRASS_CENTERS = [80, 300, 500, 720]  # Центры травы по x

TOWER_CELLS_Y = [50, 200, 350, 500]  # Y-координаты верхних границ ячеек
TOWER_WIDTH = 76
TOWER_HEIGHT = 140

# Границы и размеры панели
PANEL_Y = 600               # Y-координата начала нижней панели
BASE_Y = 581                # Y-координата, где враг наносит урон базе

# Размеры кнопок меню
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BUTTON_X = 300              # X-координата кнопок меню (по центру)

# Размеры иконок башен в панели
TOWER_ICON_WIDTH = 180
TOWER_ICON_HEIGHT = 150
TOWER_ICON_Y = 615

# Границы клика по иконкам (для выбора типа башни)
TOWER_CLICK_ZONES = [
    (40, 220),
    (300, 480),
    (560, 740),
]

import pygame


# Detect the screen size
pygame.init()

screen_info = pygame.display.Info()

SCREEN_WIDTH = screen_info.current_w
SCREEN_HEIGHT = screen_info.current_h


# Leave some space for the Windows taskbar and window borders
WIDTH = int(SCREEN_WIDTH * 0.85)
HEIGHT = int(SCREEN_HEIGHT * 0.80)

FPS = 60

TITLE = "Life Sim"

PLAYER_SPEED = 200


# Colors
GRASS = (100, 170, 90)
ROAD = (80, 80, 80)
HOUSE = (180, 130, 90)
SHOP = (80, 130, 190)
WORK = (150, 100, 180)
PARK = (80, 150, 100)

PLAYER_COLOR = (220, 60, 60)

TEXT_COLOR = (255, 255, 255)
PANEL_COLOR = (30, 30, 30)
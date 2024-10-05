# settings.py

import pygame

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
HOVER_COLOR = (255, 255, 0)
RAIN_COLOR = (0, 0, 255)

# Fonts
pygame.font.init()
FONT = pygame.font.SysFont("monospace", 35)
SMALL_FONT = pygame.font.SysFont("monospace", 25)

# Game settings
PLAYER_SIZE = 50
OBSTACLE_SIZE = 50
SPEED = 10

# Clock
CLOCK = pygame.time.Clock()

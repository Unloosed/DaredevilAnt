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

# Load images
BACKGROUND_IMAGE = pygame.image.load("assets/background.png")
ANT_IMAGE = pygame.image.load("assets/ant.png")
RAINDROP_IMAGE = pygame.image.load("assets/raindrop.png")
FLOOR_IMAGE = pygame.image.load("assets/floor.png")

# Scale images as needed
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT))
ANT_IMAGE = pygame.transform.scale(ANT_IMAGE, (PLAYER_SIZE, PLAYER_SIZE))
RAINDROP_IMAGE = pygame.transform.scale(RAINDROP_IMAGE, (OBSTACLE_SIZE, OBSTACLE_SIZE))
FLOOR_IMAGE = pygame.transform.scale(FLOOR_IMAGE, (SCREEN_WIDTH, 100))  # Adjust height as needed

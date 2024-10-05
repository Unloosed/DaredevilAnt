# main.py

import pygame
from menu import main_menu
from music import play_main_theme

# Initialize Pygame
pygame.init()

if __name__ == "__main__":
    play_main_theme()
    main_menu()

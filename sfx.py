import pygame
from settings import VOLUME

SOUND_EFFECTS_DIRECTORY = "sfx/"

DEATH_SOUND_FILE_NAME = "death_sound_effect.mp3"
DEATH_SOUND = pygame.mixer.Sound(SOUND_EFFECTS_DIRECTORY + DEATH_SOUND_FILE_NAME)

CLICK_BUTTON_SOUND_FILE_NAME = "click_button.mp3"
CLICK_BUTTON_SOUND = pygame.mixer.Sound(SOUND_EFFECTS_DIRECTORY + CLICK_BUTTON_SOUND_FILE_NAME)

HOVER_BUTTON_SOUND_FILE_NAME = "hover_button.mp3"
HOVER_BUTTON_SOUND = pygame.mixer.Sound(SOUND_EFFECTS_DIRECTORY + HOVER_BUTTON_SOUND_FILE_NAME)

def play_sound_effect(sound_effect):
    sound_effect.set_volume(VOLUME)
    sound_effect.play()
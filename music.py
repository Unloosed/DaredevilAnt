import pygame
import random

SONG_DIRECTORY = "music/"
SONGS = ["Daredevil Ant.mp3", "Circles.mp3", "Dreaming.mp3", "Hiking up a Mountain.mp3",
         "Hyperactive.mp3", "Running on Empty.mp3", "Waking Up.mp3"]

def play_main_theme():
    """Play Daredevil Ant.mp3"""
    pygame.mixer.music.load(SONG_DIRECTORY + SONGS[0])
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

def play_game_music():
    """Play a random song from music folder EXCEPT Daredevil Ant.mp3"""
    available_songs = SONGS[1:]  # exclude the first song in the list
    selected_song = random.choice(available_songs)
    pygame.mixer.music.load(SONG_DIRECTORY + selected_song)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

def stop_music():
    pygame.mixer.music.stop()

# menu.py

import sys
from settings import *
from game import game
from music import *
from sfx import *


def main_menu():
    menu = True
    while menu:
        screen.fill(BLACK)
        # screen.blit(MAIN_MENU_BACKGROUND_IMAGE, (0, 0))
        title = FONT.render("Daredevil Ant", True, WHITE)
        play_button = SMALL_FONT.render("Start Game", True, WHITE)
        highscore_button = SMALL_FONT.render("High Scores", True, WHITE)
        quit_button = SMALL_FONT.render("Quit", True, WHITE)

        play_rect = play_button.get_rect(topleft=(SCREEN_WIDTH // 2 - play_button.get_width() // 2, SCREEN_HEIGHT // 2))
        highscore_rect = highscore_button.get_rect(topleft=(SCREEN_WIDTH // 2 - highscore_button.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        quit_rect = quit_button.get_rect(topleft=(SCREEN_WIDTH // 2 - quit_button.get_width() // 2, SCREEN_HEIGHT // 2 + 100))

        # Check for hover effect
        mouse_pos = pygame.mouse.get_pos()
        if play_rect.collidepoint(mouse_pos):
            play_button = SMALL_FONT.render("Start Game", True, HOVER_COLOR)
        if highscore_rect.collidepoint(mouse_pos):
            highscore_button = SMALL_FONT.render("High Scores", True, HOVER_COLOR)
        if quit_rect.collidepoint(mouse_pos):
            quit_button = SMALL_FONT.render("Quit", True, HOVER_COLOR)

        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, SCREEN_HEIGHT // 3))
        screen.blit(play_button, play_rect.topleft)
        screen.blit(highscore_button, highscore_rect.topleft)
        screen.blit(quit_button, quit_rect.topleft)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(mouse_pos):
                    play_sound_effect(CLICK_BUTTON_SOUND)
                    play_main_theme()
                    game()
                if highscore_rect.collidepoint(mouse_pos):
                    play_sound_effect(CLICK_BUTTON_SOUND)
                    show_high_scores()
                if quit_rect.collidepoint(mouse_pos):
                    play_sound_effect(CLICK_BUTTON_SOUND)
                    pygame.quit()
                    sys.exit(0)

def show_high_scores():
    from score import load_high_scores

    high_scores = load_high_scores()
    showing = True
    while showing:
        screen.fill(BLACK)
        title = FONT.render("High Scores", True, WHITE)
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, SCREEN_HEIGHT // 3))

        menu_text = SMALL_FONT.render("Main Menu", True, WHITE)
        menu_rect = menu_text.get_rect(topleft=(SCREEN_WIDTH // 2 - menu_text.get_width() // 2, SCREEN_HEIGHT // 2 + 150))
        mouse_pos = pygame.mouse.get_pos()
        if menu_rect.collidepoint(mouse_pos):
            menu_text = SMALL_FONT.render("Main Menu", True, HOVER_COLOR)
        screen.blit(menu_text, menu_rect.topleft)

        for idx, score in enumerate(high_scores):
            score_text = SMALL_FONT.render(f"{idx + 1}. {score}", True, WHITE)
            screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2 + idx * 30))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                showing = False
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_rect.collidepoint(mouse_pos):
                    play_sound_effect(CLICK_BUTTON_SOUND)
                    main_menu()

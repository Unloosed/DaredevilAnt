# game.py

import random
import time
import sys
from settings import *
from score import save_high_score
from music import *
from sfx import *

def game():
    play_game_music()
    player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - 2 * PLAYER_SIZE]
    obstacle_list = [create_obstacle()]
    score = 0

    # Set initial direction flags
    facing_left = True
    facing_right = False

    # Set initial player direction
    ant_image = ANT_FACING_LEFT_IMAGE

    game_over = False

    # Initialize the timer (60 seconds)
    start_time = time.time()
    timer = 60

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            if facing_right:
                ant_image = ANT_FACING_LEFT_IMAGE
                facing_right = False
                facing_left = True
            player_pos[0] -= 5
        if keys[pygame.K_RIGHT] and player_pos[0] < SCREEN_WIDTH - PLAYER_SIZE:
            if facing_left:
                ant_image = ANT_FACING_RIGHT_IMAGE
                facing_right = True
                facing_left = False
            player_pos[0] += 5

        # Update the timer
        elapsed_time = int(time.time() - start_time)
        remaining_time = max(0, timer - elapsed_time)

        # Check if timer has reached zero
        if remaining_time == 0:
            game_over = True
            save_high_score(score)
            stop_music()
            play_sound_effect(DEATH_SOUND)
            game_over_screen(score)

        # Draw background and floor
        screen.blit(GAME_BACKGROUND_IMAGE, (0, 0))
        screen.blit(FLOOR_IMAGE, (0, SCREEN_HEIGHT - 100))

        # Update and draw game elements
        drop_obstacles(obstacle_list)
        score = update_obstacle_positions(obstacle_list, score, player_pos)
        draw_obstacles(obstacle_list)

        if collision_check(obstacle_list, player_pos):
            game_over = True
            save_high_score(score)
            stop_music()
            play_sound_effect(DEATH_SOUND)
            game_over_screen(score)

        # Draw player
        screen.blit(ant_image, (player_pos[0], player_pos[1]))

        # Display score and timer
        display_score(score)
        display_timer(remaining_time)

        pygame.display.update()
        CLOCK.tick(30)

def display_timer(remaining_time):
    timer_text = FONT.render(f"Time: {remaining_time}", True, RED)
    text_rect = timer_text.get_rect(topleft=(SCREEN_WIDTH - 200, 10))
    screen.blit(timer_text, text_rect.topleft)

def create_obstacle():
    x_pos = random.randint(0, SCREEN_WIDTH - OBSTACLE_SIZE)
    y_pos = 0
    return [x_pos, y_pos]

def drop_obstacles(obstacle_list):
    delay = random.random()
    if len(obstacle_list) < 10 and delay < 0.1:
        obstacle_list.append(create_obstacle())

def draw_obstacles(obstacle_list):
    for obstacle_pos in obstacle_list:
        screen.blit(RAINDROP_IMAGE, (obstacle_pos[0], obstacle_pos[1]))

def update_obstacle_positions(obstacle_list, score, player_pos):
    for idx, obstacle_pos in enumerate(obstacle_list):
        if 0 <= obstacle_pos[1] < SCREEN_HEIGHT:
            obstacle_pos[1] += SPEED

            # Check if the player is near the raindrop horizontally
            if abs(obstacle_pos[0] - player_pos[0]) < PLAYER_SIZE:
                # Increment score based on proximity
                distance = abs(obstacle_pos[1] - player_pos[1])
                score_increment = max(1, (SCREEN_HEIGHT - distance) // 50)
                score += score_increment
        else:
            obstacle_list.pop(idx)
    return score

def collision_check(obstacle_list, player_pos):
    for obstacle_pos in obstacle_list:
        if detect_collision(player_pos, obstacle_pos):
            return True
    return False

def detect_collision(player_pos, obstacle_pos):
    p_x, p_y = player_pos
    o_x, o_y = obstacle_pos
    buffer_top = -5      # Leniency for the top of the player
    buffer_bottom = -10    # Leniency for the bottom
    buffer_left = -5     # Leniency for the left
    buffer_right = -5    # Leniency for the right

    # Ignore obstacles that have passed the player
    if o_y > p_y + buffer_bottom:
        return False

    if (p_x + buffer_left <= o_x < (p_x + PLAYER_SIZE + buffer_right)) or (o_x + buffer_left <= p_x < (o_x + OBSTACLE_SIZE + buffer_right)):
        if (p_y + buffer_top <= o_y < (p_y + PLAYER_SIZE + buffer_bottom)) or (o_y + buffer_top <= p_y < (o_y + OBSTACLE_SIZE + buffer_bottom)):
            return True
    return False

def display_score(score):
    text = FONT.render(f"Score: {score}", True, RED)
    screen.blit(text, (10, 10))

def game_over_screen(score):
    from menu import main_menu

    game_over = True
    while game_over:
        screen.fill(BLACK)
        game_over_text = FONT.render("Game Over", True, RED)
        score_text = SMALL_FONT.render(f"Your Score: {score}", True, WHITE)
        retry_text = SMALL_FONT.render("Try Again", True, WHITE)
        quit_text = SMALL_FONT.render("Quit", True, WHITE)
        menu_text = SMALL_FONT.render("Main Menu", True, WHITE)

        retry_rect = retry_text.get_rect(topleft=(SCREEN_WIDTH // 2 - retry_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        quit_rect = quit_text.get_rect(topleft=(SCREEN_WIDTH // 2 - quit_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100))
        menu_rect = menu_text.get_rect(topleft=(SCREEN_WIDTH // 2 - menu_text.get_width() // 2, SCREEN_HEIGHT // 2 + 150))

        # Check for hover effect
        mouse_pos = pygame.mouse.get_pos()
        if retry_rect.collidepoint(mouse_pos):
            retry_text = SMALL_FONT.render("Try Again", True, HOVER_COLOR)
        if quit_rect.collidepoint(mouse_pos):
            quit_text = SMALL_FONT.render("Quit", True, HOVER_COLOR)
        if menu_rect.collidepoint(mouse_pos):
            menu_text = SMALL_FONT.render("Main Menu", True, HOVER_COLOR)

        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 3))
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))
        screen.blit(retry_text, retry_rect.topleft)
        screen.blit(quit_text, quit_rect.topleft)
        screen.blit(menu_text, menu_rect.topleft)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_rect.collidepoint(mouse_pos):
                    play_sound_effect(CLICK_BUTTON_SOUND)
                    game()
                if quit_rect.collidepoint(mouse_pos):
                    play_sound_effect(CLICK_BUTTON_SOUND)
                    pygame.quit()
                    sys.exit(0)
                if menu_rect.collidepoint(mouse_pos):
                    play_sound_effect(CLICK_BUTTON_SOUND)
                    play_main_theme()
                    main_menu()

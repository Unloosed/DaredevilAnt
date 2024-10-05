# game.py

import pygame
import random
from settings import *
from score import save_high_score

def game():
    player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - 2 * PLAYER_SIZE]
    obstacle_list = [create_obstacle()]
    score = 0

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos[0] -= 5
        if keys[pygame.K_RIGHT] and player_pos[0] < SCREEN_WIDTH - PLAYER_SIZE:
            player_pos[0] += 5

        # Draw background and floor
        screen.blit(BACKGROUND_IMAGE, (0, 0))
        screen.blit(FLOOR_IMAGE, (0, SCREEN_HEIGHT - 100))

        # Update and draw game elements
        drop_obstacles(obstacle_list)
        score = update_obstacle_positions(obstacle_list, score, player_pos)
        draw_obstacles(obstacle_list)

        if collision_check(obstacle_list, player_pos):
            save_high_score(score)
            game_over_screen(score)

        screen.blit(ANT_IMAGE, (player_pos[0], player_pos[1]))  # Draw player
        display_score(score)

        pygame.display.update()
        CLOCK.tick(30)

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
            if obstacle_pos[1] > player_pos[1]:
                score += 1  # Increment score as raindrops get closer
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

    if (p_x <= o_x < (p_x + PLAYER_SIZE)) or (o_x <= p_x < (o_x + OBSTACLE_SIZE)):
        if (p_y <= o_y < (p_y + PLAYER_SIZE)) or (o_y <= p_y < (o_y + OBSTACLE_SIZE)):
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
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_rect.collidepoint(mouse_pos):
                    game()
                if quit_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    quit()
                if menu_rect.collidepoint(mouse_pos):
                    main_menu()

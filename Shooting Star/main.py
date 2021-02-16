import pygame
from variables import *
import drawing1
from brain import *

pygame.init()
pygame.mixer.init()

red_rectangle = pygame.Rect(-1010, 0, 1000, 500)
yellow_rectangle = pygame.Rect(1010, 0, 1000, 500)
run = 1

while True:
    if run == 1:
        while not is_game_over:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LCTRL and len(yellow_bullets) < 3:
                        bullet = pygame.Rect(YELLOW_RECT.x + 50, YELLOW_RECT.y + 22, 10, 5)
                        yellow_bullets.append(bullet)
                        fire_sound.play()

                    if event.key == pygame.K_RCTRL  and len(red_bullets) < 3:
                        bullet = pygame.Rect(RED_RECT.x, RED_RECT.y + 22, 10, 5)
                        red_bullets.append(bullet)
                        fire_sound.play()

            for bullet in yellow_bullets:
                bullet.x += BULLET_SPEED
                if yellow_rectangle.colliderect(bullet):
                    yellow_bullets.remove(bullet)
                if RED_RECT.colliderect(bullet):
                    yellow_bullets.remove(bullet)
                    red_health -= 1
                    hit_sound.play()

            for bullet in red_bullets:
                bullet.x -= BULLET_SPEED
                if red_rectangle.colliderect(bullet):
                    red_bullets.remove(bullet)
                if YELLOW_RECT.colliderect(bullet):
                    red_bullets.remove(bullet)
                    yellow_health -= 1
                    hit_sound.play()

            HEALTH_TEXT = pygame.font.SysFont('comicsans', 40)
            RED_HEALTH_TEXT = HEALTH_TEXT.render("Health: " + str(red_health), 1, (0, 255, 0))
            YELLOW_HEALTH_TEXT = HEALTH_TEXT.render("Health: " + str(yellow_health), 1, (0, 255, 0))

            keys_pressed = pygame.key.get_pressed()

            yellow_movement(keys_pressed)
            red_movement(keys_pressed)

            pygame.display.set_caption("Space Shooter")
            pygame.draw.rect(SCREEN, (255, 255, 255), yellow_rectangle)
            pygame.draw.rect(SCREEN, (255, 255, 255), red_rectangle)
            drawing1.draw(red_bullets, yellow_bullets)
            SCREEN.blit(RED_HEALTH_TEXT, (850, 10))
            SCREEN.blit(YELLOW_HEALTH_TEXT, (10, 10))
            pygame.display.update()

            if not red_health > 0:
                win = "yellow"
                run += 1
                break
            if not yellow_health > 0:
                win = "red"
                run += 1
                break

    if run > 1:
        if win == "red":
            SCREEN.blit(red_text, (325, 200))
            # SCREEN.blit(text1, (300, 300))
            pygame.display.update()
        elif win == "yellow":
            SCREEN.blit(yellow_text, (325, 200))
            # SCREEN.blit(text1, (300, 300))
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
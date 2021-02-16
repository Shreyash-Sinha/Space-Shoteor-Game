import pygame
from variables import *

pygame.init()

def yellow_movement(keys_pressed):
    """cONTROLS THE MOVEMENT OF THE YELLOW SPACESHIP"""
    if keys_pressed[pygame.K_w] and YELLOW_RECT.y - VELOCITY > 0:
        YELLOW_RECT.y -= VELOCITY
    if keys_pressed[pygame.K_a] and YELLOW_RECT.x - 0:
        YELLOW_RECT.x -= VELOCITY
    if keys_pressed[pygame.K_s] and YELLOW_RECT.y + VELOCITY < 450:
        YELLOW_RECT.y += VELOCITY
    if keys_pressed[pygame.K_d] and YELLOW_RECT.x < BORDER.x - 50:
        YELLOW_RECT.x += VELOCITY


def red_movement(keys_pressed):
    """CONTROLS THE MOVEMENT OF THE RED SPACESHIP   """
    if keys_pressed[pygame.K_UP] and RED_RECT.y - VELOCITY > 0:
        RED_RECT.y -= VELOCITY
    if keys_pressed[pygame.K_LEFT] and RED_RECT.x - VELOCITY > BORDER.x + BORDER.width:
        RED_RECT.x -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and RED_RECT.y + VELOCITY < 450:
        RED_RECT.y += VELOCITY
    if keys_pressed[pygame.K_RIGHT] and RED_RECT.x < 950:
        RED_RECT.x += VELOCITY


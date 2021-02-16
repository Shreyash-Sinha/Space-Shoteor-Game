import pygame
from variables import *

pygame.init()

def draw(red_bullets, yellow_bullets):
    """DRAWS ALL THE THINGS ON THE SCREEN"""
    SCREEN.blit(SPACE, (0, 0))
    pygame.draw.rect(SCREEN, (0, 0, 0), BORDER)
    
    SCREEN.blit(YELLOW, YELLOW_RECT)
    SCREEN.blit(RED, RED_RECT)

    for bullet in red_bullets:
        pygame.draw.rect(SCREEN, (255, 0, 0), bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(SCREEN, (255, 255, 0), bullet)
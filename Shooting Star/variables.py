import pygame
import os

pygame.init()
pygame.font.init()
pygame.mixer.init()

WIDTH = 1000
HEIGHT = 500
is_game_over = False
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60
BORDER = pygame.Rect(WIDTH//2 - 10, 0, 20, HEIGHT)


YELLOW = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("Assets", "spaceship_yellow.png")), (50, 50)), 90)
RED = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("Assets", "spaceship_red.png")), (50, 50)), 270)
YELLOW_RECT = pygame.Rect(220, 225, 50, 50)
RED_RECT = pygame.Rect(730, 225, 50, 50)

red_bullets = []
yellow_bullets = []

red_health = 10
yellow_health = 10

VELOCITY = 5
BULLET_SPEED = 7

win = ""

WINNING_TEXt = pygame.font.SysFont('comicsans', 100)
red_text = WINNING_TEXt.render('Red Wins!!', 1, (255, 255, 0))
yellow_text = WINNING_TEXt.render('Yellow Wins!!', 1, (255, 255, 0))
respawing_text = pygame.font.SysFont('comicsans', 80)
respawn = respawing_text.render("Press 'r' to respawn", 1, (255, 255, 0))
SPACE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "space.png")), (1000, 500))


hit_sound = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
fire_sound = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))

text = pygame.font.SysFont('comicsans', 75)
text1 = text.render('Click to Play Again', 1, (255, 255, 0))
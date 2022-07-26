'''Importation'''
import black
import pygame
from random import randint

'''Initialisation'''
pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 400)

'''Constant'''
WIDTH = 1440
HEIGHT = 1020
clock = pygame.time.Clock()
STAT = "menu"

'''Creation screen'''
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JeuxVacances")

'''Images'''
#Menu
bg_menu = pygame.image.load("assets/menu/menu.png")
bg_menu = pygame.transform.scale(bg_menu, (WIDTH, HEIGHT))
play_text = pygame.image.load("assets/menu/play_text.png")

'''Variables'''
#Menu
clignotement = True

'''Boucle jeux'''
running = True
while running:

    '''Events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if STAT == "menu":
                if event.key == pygame.K_SPACE:
                    STAT = "game"
        if event.type == pygame.USEREVENT and STAT == "menu":
            if clignotement == True:
                clignotement = False
                break
            if clignotement == False:
                clignotement = True

    '''Game Engine'''
    screen.blit(screen, (0, 0))
    #Menu
    if STAT == "menu":
        screen.blit(bg_menu, (0, 0))
        if clignotement == True:
            screen.blit(play_text, (500, 500))
    #Game
    if STAT == "game":
        screen.fill((0, 0, 0))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
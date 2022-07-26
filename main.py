'''Importation'''
import pygame
from random import randint
from bird import Bird
from shoot import Shoot
from ball import Balle
from rebond import Rebond
from electric import Electric

'''Initialisation'''
pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 400)

'''Constant'''
WIDTH = 850
HEIGHT = 650
clock = pygame.time.Clock()
STAT = "menu"
LEVEL = 1
SHOT = 0

'''Creation screen'''
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JeuxVacances")

'''Images'''
#Menu
bg_menu = pygame.image.load("assets/menu/menu.png")
bg_menu = pygame.transform.scale(bg_menu, (WIDTH, HEIGHT))
play_text = pygame.image.load("assets/menu/play_text.png")
play_text = pygame.transform.scale(play_text, (264, 32))

'''Texts'''
myfont = pygame.font.Font(None, 40)
myfont_number = pygame.font.Font(None, 50)
text_shots = myfont.render("SHOTS ",True, (0, 0, 0))
text_level = myfont.render("LEVEL ",True, (0, 0, 0))
text_shots_number = myfont_number.render(str(int(SHOT)), True, (0, 0, 0))
text_level_number = myfont_number.render(str(int(LEVEL)), True, (0, 0, 0))

'''Variables'''
#Menu
clignotement = True
len_bird_death = 0

'''Instances classes'''
shoot = Shoot()
balle = Balle()

'''Creation levels'''
tab_bird_1 = []
tab_bird_1.append(Bird(400, 168, "None", False, 0, 0))
tab_bird_2 = []
tab_bird_2.append(Bird(400, 40, "left", True, 70, 735))
tab_bird_2.append(Bird(400, 168, "right", True, 70, 735))
tab_bird_3 = []
tab_bird_3.append(Bird(600, 296, "None", False, 0, 0))
tab_bird_3.append(Bird(400, 40, "None", False, 70, 300))
tab_bird_3.append(Rebond(600, 90))
tab_bird_4 = []
tab_bird_4.append(Bird(600, 296, "None", False, 0, 0))
tab_bird_4.append(Bird(400, 40, "left", True, 70, 300))
tab_bird_4.append(Bird(400, 168, "left", True, 70, 300))
tab_bird_4.append(Rebond(600, 90))
tab_bird_5 = []
tab_bird_5.append(Bird(275, 168, "left", True, 70, 275))
tab_bird_5.append(Bird(270, 168, "right", True, 270, 550))
tab_bird_5.append(Bird(735, 168, "left", True, 550, 735))
tab_bird_5.append(Bird(70, 296, "right", True, 70, 275))
tab_bird_5.append(Bird(550, 296, "left", True, 270, 550))
tab_bird_5.append(Bird(550, 296, "right", True, 550, 735))
tab_bird_5.append(Rebond(650, 90))
tab_bird_5.append(Rebond(150, 90))
tab_bird_6 = []
tab_bird_6.append(Bird(400, 40, "none", False, 0, 0))
tab_bird_6.append(Electric(420, 247, "right", 330, 500))
tab_bird_7 = []
tab_bird_7.append(Bird(400, 40, "right", True, 230, 600))
tab_bird_7.append(Electric(350, 247, "right", 200, 550))
tab_bird_7.append(Electric(450, 247, "right", 300, 650))
tab_bird_8 = []
tab_bird_8.append(Bird(390, 168, "right", True, 230, 580))
tab_bird_8.append(Electric(350, 380, "right", 200, 550))
tab_bird_8.append(Electric(400, 380, "right", 250, 600))
tab_bird_8.append(Electric(450, 380, "right", 300, 650))

tab_bird_8.append(Electric(300, 380, "right", 150, 500))
tab_bird_8.append(Electric(500, 380, "right", 350, 700))
tab_bird_8.append(Rebond(400, 90))
tab_bird_9 = []
tab_bird_10 = []
tab_bird_now = tab_bird_1

'''Creation fond jeu'''
barriere_left = pygame.image.load("assets/game/cloture.png")
barriere_right = pygame.image.load("assets/game/cloture.png")
grass = pygame.image.load("assets/game/grass.png")
grass = pygame.transform.scale(grass,(3000, 920))
fil = pygame.image.load("assets/game/fil.jpg")
fil2 = pygame.image.load("assets/game/fil.jpg")
fil3 = pygame.image.load("assets/game/fil.jpg")
fil = pygame.transform.scale(fil, (718, 15))
fil2 = pygame.transform.scale(fil2, (718, 15))
fil3 = pygame.transform.scale(fil3, (718, 15))
cadre_left = pygame.image.load("assets/game/cadre_inf.png")
cadre_left = pygame.transform.scale(cadre_left, (180, 60))
cadre_right = pygame.image.load("assets/game/cadre_inf.png")
cadre_right = pygame.transform.scale(cadre_right, (180, 60))

def calcul_len_bird(tab):
    len = 0
    for elt in tab:
        if elt.type == "bird":
            len += 1
    return len

'''Boucle jeu'''
running = True
while running:

    '''Actualisation'''
    pressed = pygame.key.get_pressed()
    text_shots_number = myfont_number.render(str(int(SHOT)), True, (0, 0, 0))
    text_level_number = myfont_number.render(str(int(LEVEL)), True, (0, 0, 0))

    '''Events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if STAT == "menu":
                if event.key == pygame.K_RETURN:
                    STAT = "game"
        if event.type == pygame.USEREVENT and STAT == "menu":
            if clignotement == True:
                clignotement = False
                break
            if clignotement == False:
                clignotement = True

    '''Games Engine'''
    #Game
    if STAT == "game":
        if shoot.can_shoot == True:
            if pressed[pygame.K_d] and shoot.rect.x <= 756:
                shoot.move_right()
                balle.rect.x += shoot.speed
            if pressed[pygame.K_q] and shoot.rect.x >= 0:
                shoot.move_left()
                balle.rect.x -= shoot.speed
        if shoot.can_shoot == True:
            if pressed[pygame.K_SPACE]:
                balle.move = True
                shoot.can_shoot = False
                SHOT += 1
                balle.direction = "UP"
        #Déplacement balle
        if balle.move == True:
            if balle.direction == "UP":
                balle.move_up()
            if balle.direction == "DOWN":
                balle.move_down()
        #Collision balle
        for bird in tab_bird_now:
            if bird.type == "bird":
                if pygame.Rect.colliderect(balle.rect, bird.rect):
                    bird.alive = False
        #Déplacement birds
        for bird in tab_bird_now:
            if bird.type == "bird":
                if bird.move == True:
                    if bird.direction == "left":
                        bird.move_left()
                    if bird.direction == "right":
                        bird.move_right()
                    if bird.rect.x <= bird.limit_left:
                        bird.direction = "right"
                    if bird.rect.x >= bird.limit_right:
                        bird.direction = "left"
        #Manage rebond
        for bird in tab_bird_now:
            if bird.type == "rebond":
                if pygame.Rect.colliderect(bird.rect, balle.rect):
                    balle.direction = "DOWN"
        if balle.direction == "DOWN" and balle.rect.y >= 510:
            shoot.can_shoot = True
            balle.direction = "NONE"
        #Manage elctric
        for bird in tab_bird_now:
            if bird.type == "electric":
                if bird.direction == "left":
                    bird.move_left()
                if bird.direction == "right":
                    bird.move_right()
                if bird.rect.x >= bird.limit_right:
                    bird.direction = "left"
                if bird.rect.x <= bird.limit_left:
                    bird.direction = "right"

    '''Affichage'''
    screen.blit(screen, (0, 0))
    #Menu
    if STAT == "menu":
        screen.blit(bg_menu, (0, 0))
        if clignotement == True:
            screen.blit(play_text, (300, 300))
    #Game
    if STAT == "game":
        screen.fill((107, 194, 218))
        screen.blit(grass, (-100, 555))
        for bird in tab_bird_now:
            if bird.type == "bird":
                if bird.alive == True:
                    screen.blit(bird.image, bird.rect)
        screen.blit(barriere_left, (-68, 20))
        screen.blit(barriere_right, (680, 20))
        screen.blit(shoot.image, shoot.rect)
        screen.blit(fil, (70, 120))
        screen.blit(fil2, (70, 250))
        screen.blit(fil3, (70, 380))
        screen.blit(cadre_left, (20, 580))
        screen.blit(cadre_right, (649, 580))
        screen.blit(text_shots, (34, 600))
        screen.blit(text_shots_number, (150, 597))
        screen.blit(text_level, (667, 600))
        screen.blit(text_level_number, (780, 597))
        screen.blit(balle.image, balle.rect)
        for bird in tab_bird_now:
            if bird.type == "rebond":
                screen.blit(bird.image, bird.rect)
        for bird in tab_bird_now:
            if bird.type == "electric":
                screen.blit(bird.image, bird.rect)
        for bird in tab_bird_now:
            if bird.type == "bird":
                if bird.alive == False:
                    len_bird_death += 1
        #Si on passe au niveau suivant
        if len_bird_death == calcul_len_bird(tab_bird_now):
            LEVEL += 1
            shoot.rect.x = 375
            shoot.rect.y = 520
            shoot.can_shoot = True
            balle.move = False
            balle.rect.x = 400
            balle.rect.y = 510
            for bird in tab_bird_now:
                if bird.type == "bird":
                    bird.alive = True
            if tab_bird_now == tab_bird_9:
                tab_bird_now = tab_bird_10
            if tab_bird_now == tab_bird_8:
                tab_bird_now = tab_bird_9
            if tab_bird_now == tab_bird_7:
                tab_bird_now = tab_bird_8
            if tab_bird_now == tab_bird_6:
                tab_bird_now = tab_bird_7
            if tab_bird_now == tab_bird_5:
                tab_bird_now = tab_bird_6
            if tab_bird_now == tab_bird_4:
                tab_bird_now = tab_bird_5
            if tab_bird_now == tab_bird_3:
                tab_bird_now = tab_bird_4
            if tab_bird_now == tab_bird_2:
                tab_bird_now = tab_bird_3
            if tab_bird_now == tab_bird_1:
                tab_bird_now = tab_bird_2
        len_bird_death = 0
        #Actualisation si perd
        if balle.rect.y <= -10:
            shoot.rect.x = 375
            shoot.rect.y = 520
            shoot.can_shoot = True
            balle.move = False
            balle.rect.x = 400
            balle.rect.y = 510
            for bird in tab_bird_now:
                if bird.type == "bird":
                    bird.alive = True
        #Actualisation si touche electric
        for bird in tab_bird_now:
            if bird.type == "electric":
                if pygame.Rect.colliderect(balle.rect, bird.rect):
                    shoot.rect.x = 375
                    shoot.rect.y = 520
                    shoot.can_shoot = True
                    balle.move = False
                    balle.rect.x = 400
                    balle.rect.y = 510
                    for bird in tab_bird_now:
                        if bird.type == "bird":
                            bird.alive = True
        #Fin du jeux (réussie level 10)
        if LEVEL == 11:
            STAT = "menu"
            LEVEL = 0
            SHOT = 0
            tab_bird_now = tab_bird_1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

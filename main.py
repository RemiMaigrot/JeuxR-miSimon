'''Importation'''
import pygame
from random import randint
from bird import Bird
from shoot import Shoot
from ball import Balle

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

'''Imtages'''
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

'''Manage Level'''
tab_bird_1 = []
tab_bird_1.append(Bird(400, 168))
tab_bird_1.append(Bird(400, 298))
tab_bird_now = tab_bird_1
tab_bird_2 = []
tab_bird_2.append(Bird(400, 130))
tab_bird_2.append(Bird(400, 168))
tab_bird_2.append(Bird(400, 298))

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

'''Boucle jeu'''
running = True
while running:

    '''Actualisation'''
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
    pressed = pygame.key.get_pressed()
    #Game
    if STAT == "game":
        if shoot.can_shoot == True:
            if pressed[pygame.K_d]:
                shoot.move_right()
                balle.rect.x += shoot.speed
            if pressed[pygame.K_q]:
                shoot.move_left()
                balle.rect.x -= shoot.speed
        if shoot.can_shoot == True:
            if pressed[pygame.K_SPACE]:
                balle.move = True
                shoot.can_shoot = False
                SHOT += 1
        #Déplacement balle
        if balle.move == True:
            balle.move_up()
        #Collision balle
        for bird in tab_bird_now:
            if pygame.Rect.colliderect(balle.rect, bird.rect):
                bird.alive = False

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
            if bird.alive == False:
                len_bird_death += 1
        #Si on passe au niveau suivant
        if len_bird_death == len(tab_bird_now):
            LEVEL += 1
            shoot.rect.x = 375
            shoot.rect.y = 520
            shoot.can_shoot = True
            balle.move = False
            balle.rect.x = 400
            balle.rect.y = 510
            for bird in tab_bird_now:
                bird.alive = True
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
                bird.alive = True

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

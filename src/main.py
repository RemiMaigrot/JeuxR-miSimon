#Importation :
import pygame
pygame.init()

#Import File :
from player import Player
from window import Screen

#Constantes :
WIDTH = 639
HEIGHT = 1080
STAT = "menu"
clock = pygame.time.Clock()

#Color :
WHITE = (255, 255, 255)
GREEN = (51, 255, 51)

#Variables :
#Menu
menu = pygame.image.load("../assets/menu.png")
fleche = pygame.image.load("../assets/fleche.png")
fleche_rect = fleche.get_rect()
fleche_rect.x = 170
fleche_rect.y = 445
choice = "game"
#Game
background = pygame.image.load("../assets/background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
myfont = pygame.font.SysFont("Arial", 30)
score_text = str(0)
score_display = myfont.render(score_text, 1, GREEN)
text_score = myfont.render("SCORE", 1, WHITE)
text_lives = myfont.render("LIVES", 1, WHITE)

#Constantes classes:
player = Player()
screen = Screen(WIDTH, HEIGHT)
player = Player()

# Boucle jeu :
running = True
while running:

    #Evènements
    for event in pygame.event.get():
        #QUIT
        if event.type == pygame.QUIT:
            running = False

        # Clavier
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if STAT == "menu":
                if event.key == pygame.K_DOWN:
                    if choice == "game":
                        fleche_rect.y = 485
                        choice = "exit"
                        break
                    if choice == "exit":
                        fleche_rect.y = 445
                        choice = "game"
                        break
                if event.key == pygame.K_UP:
                    if choice == "game":
                        fleche_rect.y = 485
                        choice = "exit"
                        break
                    if choice == "exit":
                        fleche_rect.y = 445
                        choice = "game"
                        break
                    fleche_rect.y = 445
                    choice = "game"
                if event.key == pygame.K_RETURN:
                    if choice == "game":
                        STAT = "game"
                    if choice == "exit":
                        running = False

    #Déplacement vaisseau
    #Pressed
    pressed = pygame.key.get_pressed()
    if STAT == 'game':
        if pressed[pygame.K_d]:
            player.move_right()
        if pressed[pygame.K_q]:
            player.move_left()
        score_text = str(player.score)
        score_display = myfont.render(score_text, 1, GREEN)


    # Affichage
    screen.window.blit(screen.window, (0, 0))
    if STAT == "menu":
        screen.window.blit(menu, (0, 200))
        screen.window.blit(fleche, fleche_rect)
    if STAT == "game":
        screen.window.blit(background, (0, 0))
        screen.window.blit(player.image, player.rect)
        screen.window.blit(score_display, (125, 5))
        screen.window.blit(text_score, (5, 5))
        screen.window.blit(text_lives, (400, 5))
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
import pygame

class Balle(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("assets/game/ball.png")
        self.image = pygame.transform.scale(self.image, (44, 44))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 510
        self.speed = 7
        self.move = False
        self.direction = "UP"

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed

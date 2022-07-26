import pygame

class Shoot(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("assets/game/lanceur.png")
        self.image = pygame.transform.scale(self.image, (125, 158))
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500
        self.speed = 8

    def move_right(self):
        self.rect.x += self.speed

    def move_left(self):
        self.rect.x -= self.speed

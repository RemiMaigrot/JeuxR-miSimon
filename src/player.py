import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.life = 50
        self.score = 0
        self.image = pygame.image.load("../assets/vaisseau.png")
        self.rect = self.image.get_rect()
        self.rect.x = 290
        self.rect.y = 940
        self.speed = 8

    def move_right(self):
        if self.rect.x <= 639 - 64:
            self.rect.x += self.speed

    def move_left(self):
        if self.rect.x >= 0:
            self.rect.x -= self.speed
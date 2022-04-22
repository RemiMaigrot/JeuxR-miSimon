import pygame
from random import randint

class Monster(pygame.sprite.Sprite):
    def __init__(self, type_monster):
        self.type = type_monster
        if (self.type == "green"):
            self.image = pygame.image.load("../assets/green.png")
        if (self.type == "blue"):
            self.image = pygame.image.load("../assets/blue.png")
        if (self.type == "yellow"):
            self.image = pygame.image.load("../assets/yellow.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
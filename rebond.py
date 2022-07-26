import pygame

class Rebond(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/game/aération.png")
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = "rebond"

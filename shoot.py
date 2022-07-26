import pygame

class Shoot(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("assets/game/lanceur.png")
        self.image = pygame.transform.scale(self.image, (94, 119))
        self.rect = self.image.get_rect()
        self.rect.x = 375
        self.rect.y = 520
        self.speed = 4
        self.can_shoot = True

    def move_right(self):
        if self.rect.x <= 756:
            self.rect.x += self.speed

    def move_left(self):
        if self.rect.x >= 0:
            self.rect.x -= self.speed

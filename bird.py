import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/game/bird.png")
        self.image = pygame.transform.scale(self.image, (60, 92))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.alive = True

    def move_left(self):
        self.rect.x -= self.speed

    def move_right(self):
        self.rect.x += self.speed

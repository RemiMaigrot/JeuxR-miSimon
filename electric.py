import pygame

class Electric(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, limit_left, limit_right):
        self.image = pygame.image.load("assets/game/electric.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = "electric"
        self.direction = direction
        self.limit_left = limit_left
        self.limit_right = limit_right
        self.speed = 3

    def move_left(self):
        self.rect.x -= self.speed

    def move_right(self):
        self.rect.x += self.speed

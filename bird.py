import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, move, limit_left, limit_right):
        self.image = pygame.image.load("assets/game/bird.png")
        self.image = pygame.transform.scale(self.image, (60, 92))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 3
        self.alive = True
        self.direction = direction
        self.move = move
        self.type = "bird"
        self.limit_left = limit_left
        self.limit_right = limit_right

    def move_left(self):
        self.rect.x -= self.speed

    def move_right(self):
        self.rect.x += self.speed

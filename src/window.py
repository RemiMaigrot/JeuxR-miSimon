import pygame



class Screen():
    def __init__(self, width, height):
        self.window = pygame.display.set_mode((width, height))

import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, color=(255, 255, 255)):  # Default color is white
        super().__init__()

        self.image = pygame.Surface([20, 15])
        self.image.fill(color)
        self.rect = self.image.get_rect()

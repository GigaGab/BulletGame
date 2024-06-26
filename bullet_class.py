import pygame
from colors import BLACK


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([4, 10])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 3

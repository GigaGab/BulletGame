import pygame
import random
from colors import RED

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Corrected the super() call

        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()  # Corrected the method name

    def update(self):
        # Update player position
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
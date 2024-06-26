import pygame
import random

from block_class import Block
from player_class import Player
from bullet_class import Bullet
from colors import BLUE, WHITE
# Screen dimensions
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400

# Number of blocks
NUMBER_OF_BLOCK = 50

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Sprite groups
all_sprites_group = pygame.sprite.Group()
block_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

# Create blocks
for i in range(NUMBER_OF_BLOCK):
    block = Block(BLUE)
    block.rect.x = random.randrange(SCREEN_WIDTH)
    block.rect.y = random.randrange(350)
    block_group.add(block)
    all_sprites_group.add(block)

# Create player
player = Player()
all_sprites_group.add(player)

# Game variables
done = False
clock = pygame.time.Clock()
score = 0
player.rect.y = 370

# Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            bullet = Bullet()
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y  # Corrected assignment
            all_sprites_group.add(bullet)
            bullet_group.add(bullet)

    # Update all sprites
    all_sprites_group.update()

    # Collision detection for bullets and blocks
    for bullet in bullet_group:
        block_hit_group = pygame.sprite.spritecollide(bullet, block_group, True)

        for block in block_hit_group:
            bullet_group.remove(bullet)
            all_sprites_group.remove(bullet)  # Corrected typo
            score += 5
            print(score)
        if bullet.rect.y < -10:
            bullet_group.remove(bullet)
            all_sprites_group.remove(bullet)


    screen.fill(WHITE)
    all_sprites_group.draw(screen)
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()

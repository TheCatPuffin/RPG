import pygame
from sys import exit
import time

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20,20),(0,255,255))
        self.rect = self.rect = self.image.get_rect(center=(600, 300))
        worldscreenpos = [2,2]

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.rect.centerx > 0:
                self.rect.centerx = self.rect.centerx - 1
            else:
                if worldscreenpos[0] > 1:
                    worldscreenpos[0] = worldscreenpos[0] - 1
        if keys[pygame.K_RIGHT]:
            if self.rect.centerx < 1200:
                self.rect.centerx = self.rect.centerx + 1
            else:
                if worldscreenpos[0] < 3:
                    worldscreenpos[0] = worldscreenpos[0] + 1
        if keys[pygame.K_UP]:
            if self.rect.centery > 0:
                self.rect.centery = self.rect.centery - 1
            else:
                if worldscreenpos[1] > 1:
                    worldscreenpos[1] = worldscreenpos[1] - 1
        if keys[pygame.K_DOWN]:
            if self.rect.centery > 0:
                self.rect.centery = self.rect.centery - 1
            else:
                if worldscreenpos[1] > 1:
                    worldscreenpos[1] = worldscreenpos[1] - 1
            

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
             
    
    pygame.display.update()
    clock.tick(60)

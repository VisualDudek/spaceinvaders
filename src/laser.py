from time import sleep
import pygame


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, speed=-5):
        super().__init__() 

        self.image = pygame.Surface((4,20))
        self.image.fill('white')
        self.rect = self.image.get_rect(center = pos)

        self.speed = speed #TODO: now speed depends on FPS, refactor it

    def update(self):
        self.rect.y += self.speed

    
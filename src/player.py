from re import S
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__() #TODO: need of deeper understanding

        self.image = pygame.image.load('./graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
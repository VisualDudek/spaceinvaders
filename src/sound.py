import pygame

class Sound():
    def __init__(self):
        self.volume = 0.1

        self.music = pygame.mixer.Sound('./audio/music.wav')
        self.music.set_volume(self.volume)

        self.laser_sound = pygame.mixer.Sound('./audio/laser.wav')
        self.laser_sound.set_volume(self.volume)

        self.explosion_sound = pygame.mixer.Sound('./audio/explosion.wav')
        self.explosion_sound.set_volume(self.volume)
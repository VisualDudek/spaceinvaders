import pygame

class Sound():
    def __init__(self):
        # volume setup
        self.volume = 0.1
        self.volume_fx = 1

        self.music = pygame.mixer.Sound('./audio/music.wav')
        self.music.set_volume(self.volume)

        self.laser_sound = pygame.mixer.Sound('./audio/laser.wav')
        self.laser_sound.set_volume(self.volume)

        self.explosion_sound = pygame.mixer.Sound('./audio/explosion.wav')
        self.explosion_sound.set_volume(self.volume)

        # SFX
        self.selectionClick = pygame.mixer.Sound('./audio/selectionclick.wav')
        self.selectionClick.set_volume(self.volume_fx)


    def music_up(self):
        self.volume += 0.1
        self.constrain_music_volume()
        self.music.set_volume(self.volume)
        self.selectionClick.play()

    def music_down(self):
        self.volume -= 0.1
        self.constrain_music_volume()
        self.music.set_volume(self.volume)
        self.selectionClick.play()

    def constrain_music_volume(self):
        if self.volume > 1:
            self.volume = 1
        if self.volume < 0:
            self.volume = 0
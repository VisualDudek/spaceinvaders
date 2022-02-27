from re import S
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, constraint, speed):
        super().__init__() #TODO: need of deeper understanding

        self.image = pygame.image.load('./graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos) # this is Rect object

        self.speed = speed
        self.max_x_constraint = constraint

        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 600

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()

    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = True

    def shoot_laser(self):
        print('shoot laser')

    def constraint(self): # ciekawe rozwizanie polegajace na implementacji constraints
                          #w osobnej metodzie poza get_input
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.max_x_constraint: 
            self.rect.right = self.max_x_constraint
            # z powyzszego wynika ze metoda right/left przesuwa odpowiednio caly sprite, do potwierdzenia

    def update(self):
        self.get_input()
        self.constraint()
        self.recharge()
import imp
from re import X
import pygame, sys
from player import Player
import obstacle
from alien import Alien, ExtraAlien
from random import choice, randint
from laser import Laser
from sound import Sound
from enum import Enum


class Game:
    def __init__(self) -> None:
        #Player seup
        player_sprite = Player((screen_width / 2, screen_height), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite) #TODO: co to jest?
        self.super_laser_mode = True
        self.invincible_mode = True

        # health system
        self.lives = 3
        self.live_surf = pygame.image.load('./graphics/player.png').convert_alpha()
        self.live_x_start_pos = screen_width - (self.live_surf.get_size()[0] * 2 + 20)

        # score system
        self.score = 0

        # fonts
        self.font = pygame.font.Font('./font/Pixeled.ttf', 20)
        self.font_40 = pygame.font.Font('./font/Pixeled.ttf', 40)

        # obstacle setup
        self.shape = obstacle.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstacle_amount = 4
        self.obstacle_x_positions = [num * (screen_width / self.obstacle_amount) for num in range(self.obstacle_amount)]
        self.create_multiple_obstacles(40, 480, self.obstacle_x_positions)

        # Alien setup
        self.aliens = pygame.sprite.Group()
        self.alien_setup(rows = 6, cols = 8)
        self.alien_lasers = pygame.sprite.Group()
        self.alien_speed = 0.5
        self.alien_direction = 1
        self.alien_laser_time = 800

        # Extra Alien setup
        self.extraAlien = pygame.sprite.GroupSingle()
        self.extraAlien_spawn_time = randint(400, 800)

        # Audio
        sound.music.play(loops = -1)

        # Volume display 
        self.volume_time = 0
        self.volume_timeout = 300
        self.volume_onscreen = False

    def alien_setup(self, rows, cols, x_distance = 60, y_distance = 48, x_offset = 70, y_offset = 100):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset

                if row_index == 0: alien_sprite = Alien('yellow', x, y)
                elif 1 <= row_index <= 2: alien_sprite = Alien('green', x, y)
                else: alien_sprite = Alien('red', x, y)
                self.aliens.add(alien_sprite)

    def alien_position_checker(self):
        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            if alien.rect.right >= screen_width and self.alien_direction > 0:
                self.alien_direction = -1
                self.alien_move_down(2)
            elif alien.rect.left <= 0 and self.alien_direction < 0:
                self.alien_direction = 1
                self.alien_move_down(2)

    def alien_move_down(self, distance):
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += distance

    def create_obstacle(self, x_start, y_start, offset_x):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = col_index * self.block_size + x_start + offset_x
                    y = row_index * self.block_size + y_start
                    block = obstacle.Block(self.block_size, (241,79,80), x, y)
                    self.blocks.add(block)

    def create_multiple_obstacles(self, x_start, y_start, offset):
        for offset_x in offset:
            self.create_obstacle(x_start, y_start, offset_x)

    def alien_shoot(self):
        '''Randomly choose one alien and create laser sprite on ALIENLASER event'''
        if self.aliens.sprites():

            # do not like it in this way -> poor optimalization
            for event in events:
                if event.type == ALIENLASER:
                    random_alien = choice(self.aliens.sprites()) # briliant aproach
                    laser_sprite = Laser(random_alien.rect.center, 6, screen_height)
                    self.alien_lasers.add(laser_sprite)
                    sound.laser_sound.play()
        
    def extra_alien_timer(self):
        #TODO: fix infinite ExtraAliens, check Laser class to see how it is done
        #or is it done by GroupSingle()?
        self.extraAlien_spawn_time -= 1
        if self.extraAlien_spawn_time <= 0:
            self.extraAlien.add(ExtraAlien(choice(['right', 'left']), screen_width))
            self.extraAlien_spawn_time = randint(400, 800)

    def collision_checks(self):

        # player lasers
        if self.player.sprite.lasers:  #NOT self.player.lasers
            for laser in self.player.sprite.lasers:

                # obstacle collisions
                if pygame.sprite.spritecollide(laser, self.blocks, dokill=True):
                    laser.kill()

                # alien collisions
                aliens_hit = pygame.sprite.spritecollide(laser, self.aliens, dokill=True)
                if aliens_hit:
                    for alien in aliens_hit: # bc with one laser U can hit two aliens
                        self.score += alien.value

                    if not self.super_laser_mode:
                        laser.kill()

                    sound.explosion_sound.play()

                # ExtraAlien collisions
                if pygame.sprite.spritecollide(laser, self.extraAlien, dokill=True):
                    laser.kill()
                    self.score += ExtraAlien.value
                    sound.explosion_sound.play()

        # alien lasers
        if self.alien_lasers:
            for laser in self.alien_lasers:

                # obstacle collisions
                if pygame.sprite.spritecollide(laser, self.blocks, dokill=True):
                    laser.kill()

                # player collison
                if pygame.sprite.spritecollide(laser, self.player, dokill=False):
                    laser.kill()
                    
                    if not self.invincible_mode:
                        self.lives -= 1

                    if self.lives <= 0:
                        pygame.quit()
                        sys.exit()

        # aliens
        if self.aliens:
            for alien in self.aliens:
                # obstacle collisions
                pygame.sprite.spritecollide(alien, self.blocks, dokill=True)
                #TODO: add alien vs. player collision

    def display_lives(self):
        for live in range(self.lives - 1):
            x = self.live_x_start_pos + (live * (self.live_surf.get_size()[0] + 10))
            screen.blit(self.live_surf, (x, 8))

    def display_score(self):
        score_surf = self.font.render(f'score: {self.score}', False, 'white')
        score_rect = score_surf.get_rect(topleft = (10,-10)) # what it is?
        screen.blit(score_surf, score_rect)

    def victory_message(self):
        if not self.aliens.sprites():
            victory_surf = self.font.render('You won', False, 'white')
            victory_rect = victory_surf.get_rect(center = (screen_width /2, screen_height /2))
            screen.blit(victory_surf, victory_rect)

    def pause_message(self):
        pause_surf = self.font_40.render('P A U S E', False, 'white')
        pause_rect = pause_surf.get_rect(center = (screen_width /2, screen_height /2))
        screen.blit(pause_surf, pause_rect)

    def display_volume(self):
        # display vmusic volume in the center of screen
        #with timeout

        if self.volume_onscreen:

            text = f'VOLUME: {"| " * int(sound.volume * 10)}'

            volume_surf = self.font.render(text , False, 'green')
            volume_rect = volume_surf.get_rect(center = (screen_width/2, int(screen_height * 0.7)))
            screen.blit(volume_surf, volume_rect)

            if pygame.time.get_ticks() > self.volume_time + self.volume_timeout:
                self.volume_onscreen = False

    def check_speed(self):
        '''Based on how many aliens are left and change their speed'''
        no = len(self.aliens)

        #TODO rewire if conditions, cannot execute all of them
        if no <= 45:
            self.alien_speed = 1
            self.update_alien_laser_time(800)
        if no <= 35:
            self.alien_speed = 1.5
        if no <= 25:
            self.alien_speed = 2
        if no <= 15:
            self.alien_speed = 2.5
        if no <= 5:
            self.alien_speed = 3
        if no == 1:
            self.alien_speed = 4

    def update_alien_laser_time(self, time):
        '''Update alien laser speed via change in millis time event is created in event queue'''
        if time != self.alien_laser_time:
            self.alien_laser_time = time
            pygame.time.set_timer(ALIENLASER, 0) # why first need to be set to 0?
            pygame.time.set_timer(ALIENLASER, self.alien_laser_time)


    def run(self):
        # game logic based on gamestate

        if gamestate == GameState.RUN:
            self.player.update(keys)
            self.aliens.update(self.alien_direction * self.alien_speed)
            self.alien_position_checker()
            self.check_speed()
            self.alien_shoot()
            self.alien_lasers.update()
            self.extra_alien_timer()
            self.extraAlien.update()
            self.collision_checks()
            self.display_lives()
            self.display_score()

            self.player.sprite.lasers.draw(screen) # dlaczego poprzez sprite?
            self.player.draw(screen)

            self.blocks.draw(screen)
            self.aliens.draw(screen)
            self.alien_lasers.draw(screen)
            self.extraAlien.draw(screen)
            self.victory_message()
            self.display_volume()

        elif gamestate == GameState.PAUSE:
            self.player.draw(screen)
            self.player.sprite.lasers.draw(screen) 
            self.blocks.draw(screen)
            self.aliens.draw(screen)
            self.alien_lasers.draw(screen)
            self.extraAlien.draw(screen)
            self.display_volume()
            self.pause_message()
            self.display_lives()
            self.display_score()

class CRT:
    '''Cathode Ray Tube monitor effect'''
    def __init__(self) -> None:
        self.tv = pygame.image.load('./graphics/tv.png').convert_alpha()
        self.tv = pygame.transform.scale(self.tv,(screen_width, screen_height))

    def create_crt_lines(self):
        line_height = 3
        line_amount = int(screen_height / line_height)
        for line in range(line_amount):
            y_pos = line * line_height
            pygame.draw.line(self.tv, 'black', (0, y_pos), (screen_width, y_pos), 1)


    def draw(self):
        # flicker effect
        # self.tv.set_alpha(randint(75,90))
        self.tv.set_alpha(90)

        self.create_crt_lines()
        screen.blit(self.tv,(0,0))


class KeysControl():
    def __int__(self):
        pass
    
    def update(self):
        for event in events:

            #TODO: why gamestate is unbound with == operator ???
            global gamestate
            if gamestate == GameState.RUN:
        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        sound.music_up()
                        game.volume_onscreen = True
                        game.volume_time = pygame.time.get_ticks()

                    elif event.key == pygame.K_s:
                        sound.music_down()
                        game.volume_onscreen = True
                        game.volume_time = pygame.time.get_ticks()

                    elif event.key == pygame.K_p:
                        gamestate = GameState.PAUSE
                        sound.music.stop()
                        pygame.time.set_timer(ALIENLASER, 0)

                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
            
            elif gamestate == GameState.PAUSE:

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_p:
                        gamestate = GameState.RUN
                        sound.music.play()
                        pygame.time.set_timer(ALIENLASER, game.alien_laser_time)

                    elif event.key == pygame.K_w:
                        sound.music_up()
                        game.volume_onscreen = True
                        game.volume_time = pygame.time.get_ticks()

                    elif event.key == pygame.K_s:
                        sound.music_down()
                        game.volume_onscreen = True
                        game.volume_time = pygame.time.get_ticks()


class GameState(Enum):
        RUN = 1
        PAUSE = 2

if __name__ == '__main__': #TODO: wierd if-main setup
    pygame.init()
    screen_width = 600
    screen_height = 600
    gamestate = GameState.RUN
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    sound = Sound()
    game = Game()
    crt = CRT() # what is this? -> CRT monitor effect "Cathode Ray Tube"
    keyscontrol = KeysControl()

    ALIENLASER = pygame.USEREVENT + 1   # what is tihs?
    # repeatedly create an event on th event queue
    #this event is hadled by Game.alien_shoot() method 
    pygame.time.set_timer(ALIENLASER, game.alien_laser_time)


    # game loop
    while True:
        # handle events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == ALIENLASER:
                # game.alien_shoot()
                pass

        # handle keys
        #reading in docs that maybe pygame.KEYDOWN event will be better solution?
        keys = pygame.key.get_pressed()
        keyscontrol.update()

        screen.fill((30,30,30)) #TODO: crate RGB color var
        game.run()

        # add crt effect
        crt.draw()

        # Update the full display Surface to the screen
        # pygame.display.update() this like an optimized version of .flip()
        pygame.display.flip()

        # update the clock, this should be calld once per frame. It will compute how many
        #milliseconds have passed since the previous call.
        clock.tick(60) #TODO: avoid magic numbers
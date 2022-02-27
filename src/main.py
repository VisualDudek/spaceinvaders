import pygame, sys
from player import Player
import obstacle


class Game:
    def __init__(self) -> None:
        #Player seup
        player_sprite = Player((screen_width / 2, screen_height), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite) #TODO: co to jest?

        # obstacle setup
        self.shape = obstacle.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstacle_amount = 4
        self.obstacle_x_positions = [num * (screen_width / self.obstacle_amount) for num in range(self.obstacle_amount)]
        self.create_multiple_obstacles(40, 480, self.obstacle_x_positions)

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
        
    def run(self):
        # update all spite groups
        # draw all sprite groups

        self.player.update()

        self.player.sprite.lasers.draw(screen) # dlaczego poprzez sprite?
        self.player.draw(screen)

        self.blocks.draw(screen)


if __name__ == '__main__': #TODO: wierd if-main setup
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((30,30,30)) #TODO: crate RGB color var
        game.run()

        pygame.display.flip()
        clock.tick(60) #TODO: avoid magic numbers
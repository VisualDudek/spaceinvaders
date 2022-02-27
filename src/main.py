import pygame, sys
from player import Player


class Game:
    def __init__(self) -> None:
        player_sprite = Player((screen_width / 2, screen_height))
        self.player = pygame.sprite.GroupSingle(player_sprite) #TODO: co to jest?
        
    def run(self):
        # update all spite groups
        # draw all sprite groups

        self.player.draw(screen)


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
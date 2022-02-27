import pygame, sys


class Game:
    def __init__(self) -> None:
        pass
        
    def run(self):
        # update all spite groups
        # draw all sprite groups
        pass


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
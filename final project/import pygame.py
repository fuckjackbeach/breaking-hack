import pygame
import sys
pygame.init()


class Game:
    def init(self):
        pygame.init()
        pygame.display.set_caption("Breaking Hack")
        self.screen = pygame.display.set_mode((640 , 480))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                pygame.quit
                sys.exit

            pygame.display.update()
            self.clock.tick(60)

Game().run()

#craftpix.net
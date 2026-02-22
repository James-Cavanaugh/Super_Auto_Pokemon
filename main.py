import pygame


# Basic Pygame Stuff
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0))
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
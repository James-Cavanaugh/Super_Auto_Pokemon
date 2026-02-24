import pygame
from screens import title_screen


# Basic Pygame Stuff
class Game:
    def __init__(self):
        # Regular Pygame Setup
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0))
        self.active_screen = str(self.screen)
        self.clock = pygame.time.Clock()
        self.running = True
        # Screens
        self.title_screen = title_screen.TitleScreen(self)

    def run(self, *args):
        while self.running:
            if str(self.active_screen == "Base Class"):
                self.active_screen = str(self.title_screen)
                self.title_screen.run_animations("pallet_town")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
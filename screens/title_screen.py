import pygame
import math
import json
from screens import screen

class TitleScreen(screen.Screen):
    def __init__(self, game):
        super().__init__(game)
        self.start_screens = ["pallet_town", "lacunosa_town"]
        self.circle_angle = 0

    def startup(self):
        pass

    def run_animations(self, animation_data_entry):
        with open("data/animation_data.json") as file:
            animation_data = json.load(file)
        background = pygame.image.load(animation_data[animation_data_entry]["path"])
        background = pygame.transform.scale_by(background, animation_data[animation_data_entry]["scale_factor"]).convert_alpha()
        rect = background.get_rect()
        if animation_data[animation_data_entry]["radius_factor"] == "x":
            radius = rect.width / 4
        else:
            radius = rect.height / 4

        self.circle_angle += 2 * math.pi * (0.017)
        x = rect.centerx + math.cos(self.circle_angle) * radius
        y = rect.centery + math.sin(self.circle_angle) * radius
        rect.center = (int(x), int(y))
        self.game.screen.fill((0, 0, 0))
        self.game.screen.blit(background, rect)





    def __str__(self):
        return "Title Screen"
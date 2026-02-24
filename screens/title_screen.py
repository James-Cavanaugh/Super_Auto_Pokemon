import pygame
import math
import json
from screens import screen

class TitleScreen(screen.Screen):
    def __init__(self, game):
        super().__init__(game)
        self.start_screens = ["pallet_town", "lacunosa_town"]
        self.circle_angle = 0
        self.play_button_area = None
        self.pokedex_button_area = None
        self.settings_button_area = None

    def startup(self, game):
        pygame.time.wait(1000)
        disclaimer = pygame.image.load("assets/title-screen/disclaimer.png").convert_alpha()
        disclaimer.set_alpha(0)
        screen_center = self.game.screen.get_rect().center
        rect = disclaimer.get_rect(center=screen_center)
        for i in range(0, 256, 5):
            self.game.screen.fill((0, 0, 0))
            self.game.screen.blit(disclaimer, rect)
            pygame.display.flip()
            disclaimer.set_alpha(i)
            pygame.time.wait(20)
        pygame.time.wait(2000)
        for i in range(255, -10, -5):
            self.game.screen.fill((0, 0, 0))
            self.game.screen.blit(disclaimer, rect)
            pygame.display.flip()
            disclaimer.set_alpha(i)
            pygame.time.wait(20)
        pygame.time.wait(1000)
        game.active_screen = "Title Screen"

    def run_animations(self, animation_data_entry):
        if not self.music_playing:
            pygame.mixer.music.load("assets/sound/music/littleroot_town.mp3")
            pygame.mixer.music.play(-1)
            self.music_playing = True
        try:
            with open("data/animation_data.json") as file:
                animation_data = json.load(file)
        except FileNotFoundError("how did you let ts happen"):
            pass
        background = pygame.image.load(animation_data[animation_data_entry]["path"])
        background = pygame.transform.scale_by(background, animation_data[animation_data_entry]["scale_factor"]).convert_alpha()
        screen_center = self.game.screen.get_rect().center
        rect = background.get_rect(center=screen_center)
        if animation_data[animation_data_entry]["radius_factor"] == "x":
            radius = rect.width / 5
        else:
            radius = rect.height / 5

        self.circle_angle += 2 * math.pi * 0.001
        x = rect.centerx + math.cos(self.circle_angle) * radius
        y = rect.centery + math.sin(self.circle_angle) * radius
        rect.center = (int(x), int(y))
        self.game.screen.blit(background, rect)

    def create_buttons(self):
        title_card = pygame.image.load("assets/title-screen/title_card.png")
        screen_center = self.game.screen.get_rect().center
        screen_bottom = self.game.screen.get_rect().height
        title_card_rect = title_card.get_rect(center=(screen_center[0], screen_center[1] / 2.5))
        self.game.screen.blit(title_card, title_card_rect)
        # Play Button
        play_button = pygame.image.load("assets/title-screen/start_button.png")
        play_button = pygame.transform.scale_by(play_button, 2).convert_alpha()
        play_button_rect = play_button.get_rect(center=(screen_center[0], screen_bottom / 2.25))
        self.play_button_area = play_button_rect
        self.game.screen.blit(play_button, play_button_rect)
        # PokeDex
        pokedex_button = pygame.image.load("assets/title-screen/pokedex_button.png")
        pokedex_button = pygame.transform.scale_by(pokedex_button, 2).convert_alpha()
        pokedex_button_rect = pokedex_button.get_rect(center=(screen_center[0], screen_bottom / 1.75))
        self.pokedex_button_area = pokedex_button_rect
        self.game.screen.blit(pokedex_button, pokedex_button_rect)
        # Settings
        settings_button = pygame.image.load("assets/title-screen/settings_button.png")
        settings_button = pygame.transform.scale_by(settings_button, 2).convert_alpha()
        settings_button_rect = settings_button.get_rect(center=(screen_center[0], screen_bottom / 1.42))
        self.settings_button_area = settings_button_rect
        self.game.screen.blit(settings_button, settings_button_rect)


    def __str__(self):
        return "Title Screen"
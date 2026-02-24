import pygame

# Base class to keep everything consistent with screens
class Screen:
    def __init__(self, game):
        self.game = game
        self.music_playing = False
        self.fade_opacity = 255

    def startup(self, game):
        raise NotImplementedError("startup not implemented in screen class")

    def run_animations(self, animation_data_entry):
        raise NotImplementedError("run_animation not implemented in screen class")

    def create_buttons(self):
        raise NotImplementedError("create_buttons not implemented in screen class")

    def __str__(self):
        return "Base Class"

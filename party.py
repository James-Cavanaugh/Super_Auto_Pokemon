# Class that stores 4 pokemon is a specific order set by the player
class Party:
    def __init__(self, pokemon, is_player):
        self.pokemon = pokemon
        self.is_player = is_player
        self.active = pokemon[0]
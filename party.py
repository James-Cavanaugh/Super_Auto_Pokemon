# Class that stores 4 pokemon is a specific order set by the player
class Party:
    def __init__(self, pokemon, is_player):
        self.pokemon = pokemon
        self.is_player = is_player
        self.active = pokemon[0]

    def add_pokemon(self, pokemon):
        if len(self.pokemon) < 4:
            self.pokemon.append(pokemon)
        else:
            raise AttributeError("You can't add more than 4 pokemon to a party")

    def remove_pokemon(self, pokemon):
        if pokemon in self.pokemon:
            self.pokemon.remove(pokemon)
            #TODO: Handle Pokemon coming to PC
        else:
            if self.is_player:
                raise AttributeError(f"{pokemon.capitalize()} is not in the PLAYER party")
            else:
                raise AttributeError(f"{pokemon.capitalize()} is not in the ENEMY party")

    def replace_pokemon(self, old_pokemon, new_pokemon):
        if old_pokemon in self.pokemon:
            self.pokemon[self.pokemon.index(old_pokemon)] = new_pokemon
            # TODO: Handle Pokemon coming to PC
        else:
            if self.is_player:
                raise AttributeError(f"{old_pokemon.capitalize()} cannot be REPLACED as it is not in the PLAYER party")
            else:
                raise AttributeError(f"{old_pokemon.capitalize()} cannot be REPLACED as it is not in the ENEMY party")


    def move_pokemon(self, pokemon1, pokemon2):
        if pokemon1 in self.pokemon and pokemon2 in self.pokemon:
            self.pokemon[self.pokemon.index(pokemon1)] = pokemon2
            self.pokemon[self.pokemon.index(pokemon2)] = pokemon1
        else:
            raise AttributeError(f"{pokemon1.capitalize()} or {pokemon2.capitalize()} is not in the PLAYER party to MOVE")

import json

# Pokemon Class that stores the data of a single pokemon (character)
class Pokemon:
    def __init__(self, name):
        self.name = name
        with open("../data/pokemon_index.json", "r") as f:
            data = json.load(f)
            json_data = data[name]
        self.type = json_data["type"]
        self.health = json_data["health"]
        self.damage = json_data["damage"]
        self.ability = json_data["ability"]
        self.sprite = json_data["sprite"]
        self.status = ""

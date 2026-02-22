from globals import ABILITIES

# Decorator to put abilities into global dictionary for pokemon to access at any time
def shove_into_dict(name):
    def wrapper(func):
        ABILITIES[name] = func
        return func
    return wrapper

@shove_into_dict("burn")
def burn(battle):
    pass
    # Apply burn status to enemy pokemon

@shove_into_dict("torrent")
def torrent(battle):
    pass
    # Moves do 1.5x damage when health is less than 1/2 max

@shove_into_dict("leech seed")
def leech_seed(battle):
    pass
    # Gain +1 hp per hit




print(ABILITIES)
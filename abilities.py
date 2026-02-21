from globals import ABILITIES

def shove_into_dict(name):
    def wrapper(func):
        ABILITIES[name] = func
        return func
    return wrapper

@shove_into_dict("burn")
def burn(time, dmg):
    print(f"Player is burned for {time} seconds and for {dmg} dmg")

print(ABILITIES)
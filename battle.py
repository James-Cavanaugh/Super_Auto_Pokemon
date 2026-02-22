# Class that stores all the information regarding a pokemon battle
class Battle:
    def __init__(self, player_team, enemy_team):
        self.player_team = player_team
        self.enemy_team = enemy_team
        self.player_turn = True
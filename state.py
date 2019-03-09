#resembles state for MCTS tree generation
import copy

class State(object):

    def __init__(self, player, oponent,attack_performed,card_played,parent=None):
        self.depth = 0
        self.rating=0
        self.parent=parent
        self.cards_played=card_played
        self.attacks_performed=attack_performed
        self.children=[]
        self.player_state=copy.deepcopy(player)
        self.oponent_state=copy.deepcopy(oponent)

    #TODO implement
    def generate_children(self,attacks,cards):
        self.children= []

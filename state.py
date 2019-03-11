#resembles state for MCTS tree generation
import copy

class State(object):

    def __init__(self, player, oponent,attack_performed,card_played,parent=None):
        self.depth = 0
        self.rating=0
        self.parent=parent
        self.children=[]
        self.player_state=copy.deepcopy(player)
        self.oponent_state=copy.deepcopy(oponent)

    #TODO implement
    #generates all posibble childiren states without duplicates
    def generate_children(self,attacks,cards):
        self.children= []

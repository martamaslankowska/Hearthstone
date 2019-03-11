#scratch for MCTS logic processing

import random
from state import State

from attack import PlayerAttack,WarriorAttack
from player import Player

class MCTSPlayer(Player):

    def __init__(self, name):
        super().__init__(name)

    def select_moves(self, opponent, possible_cards_to_play, possible_attacks):

        state=State(self,opponent,None, None)
        state.generate_children(possible_attacks,possible_cards_to_play)
        # cards_to_play,attacks=self.nextMove(state)
        cards_to_play = random.choice(possible_cards_to_play)
        attacks = random.choice(possible_attacks)
        return cards_to_play, attacks


    def nextMove(self,state):
        child=self.selectChild(state)
        cards_to_play = child.cards_played
        attacks = child.attack_performed
        return cards_to_play, attacks

    # performs selection
    def selectChild(self,state):
        return state.children[0]

    def ucts_search(self):
        pass

    def tree_policy(self):
        pass

    def expand(self):
        pass

    def best_child(self):
        pass

    def default_policy(self):
        pass

    def backup(self):
        pass


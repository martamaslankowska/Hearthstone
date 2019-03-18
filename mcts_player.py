# scratch for MCTS logic processing

import random
from mcts import State
from mcts import Node

from attack import PlayerAttack, WarriorAttack
from player import Player


class MCTSPlayer(Player):

    def __init__(self, name):
        super().__init__(name)

    def select_moves(self, opponent, possible_cards_to_play, possible_attacks):
        root = State('0', self, opponent)
        attacks, cards = Node.MCTS(root, 50)
        return cards, attacks

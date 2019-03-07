import copy
import random
from itertools import chain, combinations

import card
from attack import Attack, WarriorAttack, PlayerAttack


class Player(object):

    def __init__(self, name):
        self.name = name
        self.hp = 20
        self.mana = 0
        self.deck = self.prepare_deck()
        self.hand = []
        self.warriors = []
        self.punishment = 0

    def prepare_deck(self):
        deck = copy.deepcopy(card.CARDS) + copy.deepcopy(card.CARDS)
        random.shuffle(deck)
        return deck

    def hit(self):
        if len(self.deck) > 0:
            self.hand += self.deck[:1]
            self.deck = self.deck[1:]
        else:
            self.punishment += 1
            self.hp -= self.punishment

    def move(self, opponent):
        raise NotImplementedError()

    def get_possible_attacks(self, opponent):
        return self.get_attacks_from(copy.deepcopy(self.warriors), copy.deepcopy(opponent.warriors))

    def get_attacks_from(self, attacking_warriors, opponents_warriors, opponent):
        if len(attacking_warriors) == 0:
            return [[]]

        result = []
        for source_idx, source in enumerate(attacking_warriors):
            attacking_warriors_after_this_attack = attacking_warriors[:source_idx] + attacking_warriors[source_idx + 1:]
            tail_attacks = self.get_attacks_from(attacking_warriors_after_this_attack, opponents_warriors, opponent)
            result += tail_attacks  # no attack
            result += [[PlayerAttack(source, opponent)] + attack for attack in tail_attacks]
            for target_idx, target in enumerate(opponents_warriors):
                this_attack = WarriorAttack(source, target)
                target_after_this_attack = [this_attack.target_after_attack()] if not this_attack.target_dies() else []
                opponents_warriors_after_this_attack = opponents_warriors[:target_idx] + target_after_this_attack + opponents_warriors[target_idx + 1:]
                all_other_attacks = self.get_attacks_from(attacking_warriors_after_this_attack, opponents_warriors_after_this_attack, opponent)
                result += [[this_attack] + other_attacks for other_attacks in all_other_attacks]
        return result

    def get_possible_cards_to_play(self):
        def subsets(iterable):
            "subsets([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
            s = list(iterable)
            return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

        return [x for x in subsets(self.hand)
                if sum(card.mana for card in x) <= self.mana]

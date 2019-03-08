import random

from attack import PlayerAttack
from player import Player


class RandomPlayer(Player):

    def __init__(self, name):
        super().__init__(name)

    def select_moves(self, opponent, possible_cards_to_play, possible_attacks):
        cards_to_play = random.choice(possible_cards_to_play)
        attacks = random.choice(possible_attacks)
        return cards_to_play, attacks


class AggressivePlayer(Player):

    def __init__(self, name):
        super().__init__(name)

    def select_moves(self, opponent, possible_cards_to_play, possible_attacks):
        cards_to_play = self.pick_best_cards(possible_cards_to_play)
        attacks = self.find_suitable_attack(possible_attacks)
        return cards_to_play, attacks

    def find_suitable_attack(self, attacks):
        best_attack = None
        for attack in attacks:
            if all(isinstance(att, PlayerAttack) for att in list(attack)):
                best_attack = attack
        return best_attack or ()  # in case None value

    def pick_best_cards(self, cards_combinations):
        greatest_attack, cards_combination = 0, None
        for cards in cards_combinations:
            attack_value = sum(card.attack for card in list(cards))
            if attack_value > greatest_attack:
                greatest_attack = attack_value
                cards_combination = cards
        return cards_combination or ()  # in case None value



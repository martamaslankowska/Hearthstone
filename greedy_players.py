import random

from attack import PlayerAttack, WarriorAttack
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
            if all(isinstance(att, PlayerAttack) for att in attack):
                best_attack = attack
        return best_attack or ()  # in case None value

    def pick_best_cards(self, cards_combinations):
        greatest_attack, cards_combination = 0, None
        for cards in cards_combinations:
            attack_value = sum(card.attack for card in cards)
            if attack_value > greatest_attack:
                greatest_attack = attack_value
                cards_combination = cards
        return cards_combination or ()  # in case None value


class ControllingPlayer(Player):

    def __init__(self, name):
        super().__init__(name)

    def select_moves(self, opponent, possible_cards_to_play, possible_attacks):
        cards = self.pick_card(possible_cards_to_play)
        attacks = self.find_attack(opponent, possible_attacks)
        return cards, attacks

    def find_attack(self, opponent, attacks):
        if (opponent.warriors != [] and self.warriors != []):
            return self.find_attack_on_warriors(
                [att_seq for att_seq in attacks if all(isinstance(att, WarriorAttack) for att in list(att_seq))])
        else:
            return self.find_attack_on_player(attacks)

    # returns attack sequence maximizing difference of opponent's hp damage and player's hp damage
    def find_attack_on_warriors(self, attacks):
        best_attack = None
        if attacks:
            best_attack_diff = -1000
            for attack in attacks:
                counted_attack_diff = self.warriors_damage_difference(attack)
                if counted_attack_diff >= best_attack_diff:
                    best_attack = attack
                    best_attack_diff = counted_attack_diff
        return best_attack or ()

    def find_attack_on_player(self, attacks):
        best_attack = None
        damage_sum = 0
        for attack in attacks:
            counted_sum = sum([att.source.attack for att in attack])
            if counted_sum > damage_sum:
                best_attack = attack
                damage_sum = counted_sum
        return best_attack or ()

    # just greatest attack
    def pick_card(self, cards_combinations):
        greatest_attack, cards_combination = 0, None
        for cards in cards_combinations:
            attack_value = sum(card.attack for card in cards)
            if attack_value > greatest_attack:
                greatest_attack = attack_value
                cards_combination = cards
        return cards_combination or ()

    # return max([(cards, sum(cards.attack)) for cards cards_combinations], lambda x: x[1], default=())

    def warriors_damage_difference(self, attack_seq):
        damage_diff = 0
        for att in attack_seq:
            damage_diff += att.target.hp if att.target.hp < att.source.attack else att.source.attack
            damage_diff -= att.source.hp if att.source.hp < att.target.attack else att.target.attack
        return damage_diff

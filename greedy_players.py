import random

from player import Player


class RandomPlayer(Player):

    def __init__(self, name):
        super().__init__(name)

    def move(self, opponent, possible_cards_to_play, possible_attacks):
        random.shuffle(possible_cards_to_play)
        random.shuffle(possible_attacks)

        attacks = possible_attacks[0]
        self.attack_opponent(attacks, opponent)
        cards_to_play = possible_cards_to_play[0]
        self.play_cards(cards_to_play)



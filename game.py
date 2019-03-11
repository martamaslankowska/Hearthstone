from player import *
from card import Card
import card
import random
import copy


class Game(object):

    def __init__(self, first_player, second_player):
        self.move = 0
        self.active_player = first_player
        self.inactive_player = second_player

    def prepare_game(self):
        self.active_player.hand = self.active_player.deck[:3]
        self.active_player.deck = self.active_player.deck[3:]
        self.inactive_player.hand = self.inactive_player.deck[:4]
        self.inactive_player.deck = self.inactive_player.deck[4:]
        print(f'{self.active_player} has 3 cards and {self.inactive_player} has 4 cards in hand.')

    def game_play(self):
        print(f'{self.active_player.name} starts the game.')
        self.prepare_game()
        while not self.finished():  # active player move
            self.move += 1
            self.active_player.mana = int(min((self.move+1)/2, 10))
            self.active_player.hit()
            if self.finished():  # players hp = 0 after hitting empty deck
                break
            print(f'\nMOVE nr {self.move} - round {int((self.move+1)/2)}')
            print(u'Time for {} with {}\u2661 to move... ({}\u27E1)'.format(self.active_player.name, self.active_player.hp, self.active_player.mana))
            print(f'  HAND: {self.active_player.hand}')
            print(f'  WARRIORS: {self.active_player.warriors}')
            cards, attacks = self.active_player.get_possible_moves(self.inactive_player)
            chosen_cards, chosen_attacks = self.active_player.select_moves(self.inactive_player, cards, attacks)
            self.active_player.make_moves(self.inactive_player, chosen_cards, chosen_attacks)
            self.swap_players()
        print(f'\n{self.winner().name} WINS THE GAME :)\n')
        return self.winner()

    def finished(self):
        return self.active_player.hp <= 0 or self.inactive_player.hp <= 0

    def winner(self):
        assert(self.finished())
        if self.active_player.hp > 0:
            return self.active_player
        else:
            return self.inactive_player

    def swap_players(self):
        self.active_player, self.inactive_player = self.inactive_player, self.active_player

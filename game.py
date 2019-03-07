from player import *
from card import Card
import card
import random
import copy


class Game(object):

    def __init__(self, first_player_name, second_player_name):
        self.move = 0
        self.active_player = Player(first_player_name)
        self.inactive_player = Player(second_player_name)

    def prepare_game(self):
        self.active_player.hand = self.active_player.deck[:3]
        self.active_player.deck = self.active_player.deck[3:]
        self.inactive_player.hand = self.inactive_player.deck[:4]
        self.inactive_player.deck = self.inactive_player.deck[4:]

    def game_play(self):
        while not self.finished():  # active player move
            self.move += 1
            self.active_player.mana = min((self.move+1)/2, 10)
            self.active_player.hit()
            self.active_player.move(self.inactive_player)
            self.swap_players()
        return self.winner()

    def finished(self):
        return self.active_player.hp == 0 or self.inactive_player.hp == 0

    def winner(self):
        assert(self.finished())
        if self.active_player.hp > 0:
            return self.active_player
        else:
            return self.inactive_player

    def swap_players(self):
        self.active_player, self.inactive_player = self.inactive_player, self.active_player

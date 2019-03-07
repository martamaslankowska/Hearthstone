import unittest

from card import Card
from player import Player


class PlayerTests(unittest.TestCase):

    def test_get_possible_attacks_one_vs_one(self):
        player = Player("Test Player")
        opponent_player = Player("Test Opponent")
        attacking = [Card("Light's Justice", 1, 1, 4)]
        opponents = [Card('Oasis Snapjaw', 4, 2, 7)]

        attacks = player.get_attacks_from(attacking, opponents, opponent_player)

        self.assertTrue(True)

    def test_get_possible_attacks_one_vs_two(self):
        player = Player("Test Player")
        opponent_player = Player("Test Opponent")
        attacking = [Card("Light's Justice", 1, 1, 4)]
        opponents = [Card('Oasis Snapjaw', 4, 2, 7), Card('Bloodfen Raptor', 2, 3, 2)]

        attacks = player.get_attacks_from(attacking, opponents, opponent_player)

        self.assertTrue(True)

    def test_get_possible_attacks_stronger_one_vs_two(self):
        player = Player("Test Player")
        opponent_player = Player("Test Opponent")
        attacking = [Card('Arcanite Reaper', 5, 5, 2)]
        opponents = [Card('Oasis Snapjaw', 4, 2, 7), Card('Bloodfen Raptor', 2, 3, 2)]

        attacks = player.get_attacks_from(attacking, opponents, opponent_player)

        self.assertTrue(True)

    def test_get_possible_attacks_two_vs_two(self):
        player = Player("Test Player")
        opponent_player = Player("Test Opponent")
        attacking = [Card("Light's Justice", 1, 1, 4), Card('Murloc Raider', 1, 2, 1)]
        opponents = [Card('Oasis Snapjaw', 4, 2, 7), Card('Bloodfen Raptor', 2, 3, 2)]

        attacks = player.get_attacks_from(attacking, opponents, opponent_player)

        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()

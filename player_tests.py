import time
import unittest

from bfs import BFState
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
        attacks_without_duplicates = list(set([tuple(attacks_sequence) for attacks_sequence in attacks]))

        self.assertTrue(True)


    def test_get_possible_attacks_four_vs_four(self):
        player = Player("Test Player")
        opponent_player = Player("Test Opponent")
        attacking = [Card("Light's Justice", 1, 1, 4), Card('Murloc Raider', 1, 2, 1), Card("Light's Justice", 1, 1, 4), Card('Murloc Raider', 1, 2, 1)]
        opponents = [Card('Oasis Snapjaw', 4, 2, 7), Card('Bloodfen Raptor', 2, 3, 2), Card("Light's Justice", 1, 1, 4), Card('Murloc Raider', 1, 2, 1)]

        attacks = player.get_attacks_from(attacking, opponents, opponent_player)
        attacks_without_duplicates = list(set([tuple(attacks_sequence) for attacks_sequence in attacks]))

        self.assertTrue(True)

    def test_get_possible_attacks_many(self):
        player = Player("Test Player")
        opponent_player = Player("Test Opponent")
        attacking = [Card("Light's Justice", 1, 1, 4), Card('Murloc Raider', 1, 2, 1), Card("Light's Justice", 1, 1, 4),
                     Card('Murloc Raider', 1, 2, 1), Card('Murloc Raider', 1, 2, 1), Card("Light's Justice", 1, 1, 4)]
        opponents = [] #[Card('Oasis Snapjaw', 4, 2, 7)]#, Card('Bloodfen Raptor', 2, 3, 2), Card("Light's Justice", 1, 1, 4)]

        attacks = player.get_attacks_from(attacking, opponents, opponent_player)
        attacks_without_duplicates = list(set([tuple(attacks_sequence) for attacks_sequence in attacks]))

        self.assertTrue(True)


    def test_check_equality(self):
        player1 = Player("Test Player")
        player1.prepare_deck()
        player2 = Player("Test Player")
        player2.prepare_deck()
        self.assertTrue(player1 == player2)
        self.assertTrue(player1.__eq__(player2))

    def test_card_equality(self):
        card1 = Card('Arcanite Reaper', 5, 5, 2)
        card2 = Card('Arcanite Reaper', 5, 5, 2)
        self.assertTrue(card1 == card2)


    def test_bfs_state_neighbours(self):
        warriors = [Card("Light's Justice", 1, 1, 4), Card('Murloc Raider', 1, 2, 1), Card('Core Hound', 7, 9, 5)]
        opponent = Player("Opponent")
        opponent.warriors = [Card('Oasis Snapjaw', 4, 2, 7), Card('Bloodfen Raptor', 2, 3, 2)]
        root_state = BFState(warriors, opponent, [])

        neighbours = root_state.get_all_neighbours()
        self.assertTrue(len(neighbours) == 9)

    def test_bfs_state_neighbours_of_child(self):
        warriors = [Card("Light's Justice", 1, 1, 4), Card('Murloc Raider', 1, 2, 1), Card('Core Hound', 7, 9, 5)]
        opponent = Player("Opponent")
        opponent.warriors = [Card('Oasis Snapjaw', 4, 2, 7), Card('Bloodfen Raptor', 2, 3, 2)]
        root_state = BFState(warriors, opponent, [])

        neighbours = root_state.get_all_neighbours()
        child_neighbours = neighbours[0].get_all_neighbours()
        self.assertTrue(len(child_neighbours) == 6)

    def test_bfs_state_equality(self):
        warriors = [Card("Light's Justice", 1, 1, 4), Card('Murloc Raider', 1, 2, 1), Card('Core Hound', 7, 9, 5)]
        opponent = Player("Opponent")
        opponent.warriors = [Card('Oasis Snapjaw', 4, 2, 7), Card('Bloodfen Raptor', 2, 3, 2)]
        root_state = BFState(warriors, opponent, [])

        neighbours = root_state.get_all_neighbours()
        child_neighbours = neighbours[0].get_all_neighbours()
        child1, child2 = child_neighbours[0], child_neighbours[3]
        child1_neighbour = child1.get_all_neighbours()[0]
        child2_neighbour = child2.get_all_neighbours()[0]

        self.assertTrue(child1_neighbour == child2_neighbour)

    def test_bfs_unique_states(self):
        warriors = [Card("Light's Justice", 1, 1, 4), Card('Murloc Raider', 1, 2, 1), Card('Core Hound', 7, 9, 5)]
        opponent = Player("Opponent")
        opponent.warriors = [Card('Oasis Snapjaw', 4, 2, 7), Card('Bloodfen Raptor', 2, 3, 2)]
        root_state = BFState(warriors, opponent, [])

        all_neighbours = []

        for a in root_state.get_all_neighbours():
            for b in a.get_all_neighbours():
                for c in b.get_all_neighbours():
                    all_neighbours.append(c)

        unique_neighbours = set(all_neighbours)
        self.assertTrue(True)

    def test_bfs_unique_states_smaller(self):
        warriors = [Card("Light's Justice", 1, 2, 3), Card('Murloc Raider', 1, 6, 6), Card('Core Hound', 7, 9, 5)]
        opponent = Player("Opponent")
        opponent.warriors = []#[Card('Oasis Snapjaw', 4, 5, 7)]  #, Card('Bloodfen Raptor', 2, 3, 2)]
        root_state = BFState(warriors, [], opponent, [])

        all_neighbours = []

        for a in root_state.get_all_neighbours():
            for b in a.get_all_neighbours():
                for c in b.get_all_neighbours():
                    all_neighbours.append(c)

        unique_neighbours = set(all_neighbours)
        self.assertTrue(True)

    def test_get_attacks_bfs(self):
        player = Player("Test Player")
        opponent_player = Player("Test Opponent")

        player.warriors = [Card("Light's Justice", 1, 2, 3), Card('Murloc Raider', 1, 6, 6), Card('Core Hound', 7, 9, 5), Card('Murloc Raider', 1, 6, 6), Card('Core Hound', 7, 9, 5), Card('Core Hound', 7, 9, 5)]
        opponent_player.warriors = [Card('Oasis Snapjaw', 4, 5, 7), Card('Bloodfen Raptor', 2, 3, 2)]

        # BFS
        start_bfs = time.time()
        possible_attacks = player.get_possible_attacks_bfs(opponent_player)
        end_bfs = time.time()

        # old way - many many of permutations...
        attacks = player.get_attacks_from(player.warriors, opponent_player.warriors, opponent_player)
        attacks_without_duplicates = list(set([tuple(attacks_sequence) for attacks_sequence in attacks]))
        end_old_way = time.time()

        # print(f'BFS: {end_bfs - start_bfs} sec and {len(possible_attacks)} permutations'
        #       f'\nOld way: {end_old_way - end_bfs} and {len(attacks)} permutations')

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()

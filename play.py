from game import Game
from greedy_players import RandomPlayer, AggressivePlayer, ControllingPlayer
from mcts_player import MCTSPlayer

import random

if __name__ == '__main__':
    # random.seed(17)

    player1 = RandomPlayer("Random player")
    player2 = MCTSPlayer("MCTS player")
    # player1 = AggressivePlayer("Aggressive player")
    # player2 = ControllingPlayer("Controlling player")

    # player1.verbose=True
    # player2.verbose=True

    game = Game(player1, player2, verbose=True)
    winner = game.game_play()



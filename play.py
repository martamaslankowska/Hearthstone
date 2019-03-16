from game import Game
from greedy_players import RandomPlayer, AggressivePlayer, ControllingPlayer
from mcts_player import MCTSPlayer

import random

if __name__ == '__main__':
    # random.seed(17)

    player1 = RandomPlayer("Player 1")
    player2 = MCTSPlayer("Player 2")
    # player1.verbose=True
    # player2.verbose=True

    game = Game(player1, player2,verbose=True)
    winner = game.game_play()



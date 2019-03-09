from game import Game
from greedy_players import RandomPlayer, AggressivePlayer, ControllingPlayer

import random

if __name__ == '__main__':
    random.seed(17)

    player1 = ControllingPlayer("Player 1")
    player2 = RandomPlayer("Player 2")

    game = Game(player1, player2)
    winner = game.game_play()

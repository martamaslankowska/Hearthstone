from game import Game
from greedy_players import RandomPlayer, AggressivePlayer

import random

if __name__ == '__main__':
    random.seed(17)

    player1 = AggressivePlayer("Player 1")
    player2 = RandomPlayer("Player 2")

    game = Game(player1, player2)
    winner = game.game_play()

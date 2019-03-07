from game import Game
from greedy_players import RandomPlayer

if __name__ == '__main__':
    player1 = RandomPlayer("Player 1")
    player2 = RandomPlayer("Player 2")

    game = Game(player1, player2)
    winner = game.game_play()

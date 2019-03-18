# resembles state for MCTS tree generation
import copy
import numpy as np
import game as gm
import greedy_players as greedy
import random
import itertools


# określa stan węzła drzewa gry = stan planszy, mapuje się do gry
class State(object):

    def __init__(self, id, player, opponent, attack_performed=None, card_played=None):
        self.id = id
        self.cards_played = card_played  # te które doprowadziły do stanu
        self.attacks_performed = attack_performed  # te które doprowadziły do stanu
        self.player = player  # stan określa stan gracza
        self.opponent = opponent  # i stan przeciwnika
        self.substates = [] # możliwe podstany z danego stanu

    def __eq__(self, other):
        return self.id == other.id

    # wszystkie podstany
    def generate_substates(self):
        ident = 0
        possible_cards, possible_attacks = self.player.get_possible_moves(self.opponent)
        if possible_attacks==[]:
            possible_attacks.append([])
        combinations=list(itertools.product(possible_cards, possible_attacks))
        substates_collection=[]
        for elems in combinations:
            print(' combination:', elems)
            new_player = copy.deepcopy(self.player)
            new_opponent = copy.deepcopy(self.opponent)
            cards=elems[0]
            attack=elems[1]
            new_player.make_moves(new_opponent, cards, attack)
            substate = State(self.id + '.' + str(ident), new_opponent, new_player, attack, cards)
            substates_collection.append(substate)
            ident += 1
        return substates_collection

    # tu można bedzie zmieniać heurystyki playoutów
    def simulate_playout(self):
        # player_random=greedy.RandomPlayer.copy(self.player)
        # oponnent_random=greedy.RandomPlayer.copy(self.opponent)
        # game=gm.Game(player_random,oponnent_random)
        # game.game_play()
        # winner=game.winner()
        # return winner.name
        return self.player.name


# określa węzeł drzewa gry - na nim wykonywane są operacje zwiazane z budowaniem i przechodzeniem drzewa
# lepiej rozdzielić od stanu
class Node(object):

    nr_of_playouts = 5  # number of playouts played every time

    def __init__(self, parent=None, state=None):
        self.parent = parent
        self.state=state
        self.childNodes = []
        self.wins = 0  # liczba zwycięstw z węzła lub dzieci
        self.playouts = 0  # liczba wykoanych playoutów z węzła lub dzieci
        self.untriedSubstates = state.generate_substates()  # stany do ekspansji

    # odpowiada za wybór węzła przy przechodzeniu drzewa przy wykorzystaniu miary UCB1
    def selection(self):
        s = sorted(self.childNodes, key=lambda c: c.wins / c.playouts + np.sqrt(2 * np.log(self.playouts) / c.playouts))[-1]
        return s

    def append_child(self, substate):
        n = Node(parent=self, state=substate)
        self.untriedSubstates.remove(substate)
        self.childNodes.append(n)
        return n

    def update_params(self, nr_of_playouts, result):
        self.playouts += nr_of_playouts
        self.wins += result

    @staticmethod
    def MCTS(root_state, iterations_count):

        rootnode = Node(state=root_state)

        for i in range(iterations_count):
            print(f'  MCTS ITERATION {i}')
            node = rootnode
            state=node.state
            # state = root_state.clone()

            # Przechodzenie w dół
            while node.untriedSubstates == [] and node.childNodes != []:
                node = node.selection()
                state=node.state

            #Zatrzymałem się w liściu lub na węźle, z którego można zrobić ekspansję

            # Ekspansja
            if node.untriedSubstates != []:
                chosen_substate = random.choice(node.untriedSubstates)
                state = chosen_substate
                node = node.append_child(state)
            #Teraz jestem w liściu

            #Playout
            playout_winns = 0
            for i in range(node.nr_of_playouts):
                playout_winner = state.simulate_playout()
                playout_winns += 1 if playout_winner == node.state.player.name else 0  #1 dla zwycięzcy 0 dla przegranego
            print(f'    playout stats: {playout_winns}/{node.nr_of_playouts}')

            # Backpropagation
            while node != None:  # aż do korzenia
                node.update_params(node.nr_of_playouts, playout_winns)
                node = node.parent

        chosen_root_subnode=sorted(rootnode.childNodes, key=lambda c: c.wins/c.playouts)[-1]
        return chosen_root_subnode.state.attacks_performed,chosen_root_subnode.state.cards_played

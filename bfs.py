import copy

from attack import PlayerAttack, WarriorAttack


class BFState(object):

    def __init__(self, warriors, warriors_inactive, opponent, previous_attacks):
        self.warriors_active = warriors
        self.warriors_inactive = warriors_inactive
        self.opponent = opponent
        self.opponents_warriors = self.opponent.warriors
        self.previous_attacks = previous_attacks

    def __eq__(self, obj):
        return isinstance(obj, BFState) and set(obj.warriors_active) == set(self.warriors_active) and \
               set(obj.warriors_inactive) == set(self.warriors_inactive) and \
               set(obj.opponents_warriors) == set(self.opponents_warriors) and obj.opponent.hp == self.opponent.hp

    def __hash__(self):
        return hash((frozenset(self.warriors_active), frozenset(self.warriors_inactive),
                     frozenset(self.opponents_warriors), self.opponent.hp))

    def get_all_neighbours(self):
        neighbours = []
        for warrior in self.warriors_active:
            new_active_warriors = [w for w in self.warriors_active if w != warrior]
            # attacking Player by each warrior
            opponent_with_less_hp = copy.deepcopy(self.opponent)
            opponent_with_less_hp.hp -= warrior.attack
            player_attack = PlayerAttack(warrior, self.opponent)
            neighbours.append(BFState(new_active_warriors, self.warriors_inactive + [warrior], opponent_with_less_hp,
                                      self.previous_attacks + [player_attack]))

            # attacking opponents warrior by each warrior
            for opponent_warrior in self.opponents_warriors:
                warrior_attack = WarriorAttack(warrior, opponent_warrior)

                warrior_after_attack = copy.deepcopy(warrior)
                warrior_after_attack.hp = 0 if warrior_attack.source_dies() else warrior_attack.source_after_attack().hp

                opponent_warrior_after_attack = copy.deepcopy(opponent_warrior)
                opponent_warrior_after_attack.hp = 0 if warrior_attack.target_dies() else warrior_attack.target_after_attack().hp
                opponents_warriors_left = [w for w in self.opponents_warriors if w != opponent_warrior]

                inactive_warriors = copy.deepcopy(self.warriors_inactive)
                if not warrior_attack.source_dies():
                    inactive_warriors += [warrior_after_attack]
                if not warrior_attack.target_dies():
                    opponents_warriors_left += [opponent_warrior_after_attack]

                opponent_with_less_warriors = copy.deepcopy(self.opponent)
                opponent_with_less_warriors.warriors = opponents_warriors_left
                neighbours.append(BFState(new_active_warriors, inactive_warriors, opponent_with_less_warriors,
                                          self.previous_attacks + [warrior_attack]))

        return neighbours
